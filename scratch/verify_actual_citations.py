import os
import re
import glob
import subprocess
import json

# 1. Obter todas as chaves de citação usadas nos arquivos .tex reais do artigo
tex_files = [
    'latex/abstract.tex',
    'latex/sections/01_Introduction.tex',
    'latex/sections/02_Background.tex',
    'latex/sections/03_Empirical_Evaluation.tex',
    'latex/sections/04_Experiment_Planning.tex',
    'latex/sections/05_Results.tex',
    'latex/sections/06_analysis.tex',
    'latex/sections/06.2_Sentiments.tex',
    'latex/sections/07_Threats_Validity.tex',
    'latex/sections/08_Related_Work.tex',
    'latex/sections/09_Conclusion.tex'
]

cited_keys = set()
for tf in tex_files:
    if not os.path.exists(tf):
        print(f"Aviso: Arquivo {tf} não encontrado!")
        continue
    try:
        content = open(tf, 'r', encoding='utf-8').read()
        # Procura por \cite{key1, key2}, \citep{...}, \citet{...} etc
        cites = re.findall(r'\\cite[a-zA-Z]*\*?\{([^}]+)\}', content)
        for cite in cites:
            keys = [k.strip() for k in cite.split(',')]
            cited_keys.update(keys)
    except Exception as e:
        print(f"Erro ao ler {tf}: {e}")

print(f"Identificadas {len(cited_keys)} chaves únicas citadas no artigo real.")

# 2. Ler o bibliography.bib e mapear chaves para títulos e DOIs
bib_content = open('latex/bibliography.bib', 'r', encoding='utf-8').read()
# Divisão aproximada por entradas
entries = bib_content.split('@')

bib_map = {} # key -> {title, doi}
for entry in entries:
    if not entry.strip():
        continue
    # ex: inproceedings{guzman2014,
    match_key = re.search(r'^[a-zA-Z]+\s*\{([^,]+),', entry)
    if match_key:
        key = match_key.group(1).strip()
        
        # extrair título
        title = ""
        match_title = re.search(r'title\s*=\s*[\{"](.*?)(?:[\}"]\s*,|[\}"]\s*\n)', entry, re.IGNORECASE | re.DOTALL)
        if match_title:
            t = match_title.group(1)
            clean_t = re.sub(r'[\{\}\n]', ' ', t).strip()
            title = re.sub(r'\s+', ' ', clean_t)
            
        # extrair doi
        doi = ""
        match_doi = re.search(r'doi\s*=\s*[\{"](.*?)(?:[\}"]\s*,|[\}"]\s*\n)', entry, re.IGNORECASE | re.DOTALL)
        if match_doi:
            doi = match_doi.group(1).strip()
            # Limpar prefixos comuns se houver
            doi = re.sub(r'^https?://(?:dx\.)?doi\.org/', '', doi)
            
        bib_map[key] = {'title': title, 'doi': doi}

# 3. Classificar e validar cada chave
validation_results = {}
dois_to_query = []
keys_with_doi = []
keys_without_doi = []

for key in cited_keys:
    if key in bib_map:
        info = bib_map[key]
        if info['doi']:
            dois_to_query.append(info['doi'])
            keys_with_doi.append(key)
        else:
            keys_without_doi.append(key)
    else:
        validation_results[key] = {
            'title': "[Chave não encontrada no .bib]",
            'doi': "",
            'status': "ERRO: Citação no texto mas ausente no .bib",
            'openalex_id': ""
        }

# Executar buscas em lote de DOIs usando a CLI do OpenAlex
openalex_dir = '/home/tassio/.gemini/config/plugins/science/skills/literature_search_openalex'

# Dividir DOIs em lotes de 20 para evitar limites na linha de comando
def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

found_dois = {} # doi -> openalex_id, title

print(f"Validando {len(dois_to_query)} DOIs em lotes...")
for batch in chunks(dois_to_query, 20):
    doi_filter = "|".join(batch)
    cmd = [
        'bash', '-c',
        f'export PATH="$HOME/.local/bin:$PATH" && uv run scripts/openalex_cli.py filter works --filter "doi:{doi_filter}" --per-page 100'
    ]
    try:
        res = subprocess.run(cmd, cwd=openalex_dir, capture_output=True, text=True, check=True)
        data = json.loads(res.stdout)
        results = data.get('results', [])
        for work in results:
            w_doi = work.get('doi', '')
            if w_doi:
                w_doi_clean = re.sub(r'^https?://(?:dx\.)?doi\.org/', '', w_doi).strip()
                found_dois[w_doi_clean.lower()] = {
                    'id': work.get('id', ''),
                    'title': work.get('display_name', '')
                }
    except Exception as e:
        print(f"Erro ao buscar lote de DOIs: {e}")

# Mapear os resultados com DOI
for key in keys_with_doi:
    info = bib_map[key]
    doi_clean = info['doi'].lower()
    if doi_clean in found_dois:
        validation_results[key] = {
            'title': info['title'],
            'doi': info['doi'],
            'status': "Válido (Encontrado via DOI)",
            'openalex_id': found_dois[doi_clean]['id']
        }
    else:
        # Se não achou pelo DOI, tentar pelo título usando resolve
        keys_without_doi.append(key)

# Tratar os sem DOI ou que falharam no DOI (busca por título)
print(f"Validando {len(keys_without_doi)} citações individualmente pelo título...")
for key in keys_without_doi:
    if key in validation_results and "Válido" in validation_results[key]['status']:
        continue # Já resolvido
        
    info = bib_map.get(key, {'title': '', 'doi': ''})
    title = info['title']
    if not title:
        continue
        
    # Fazer resolve works pelo título do artigo
    # Escapar aspas duplas no título
    title_escaped = title.replace('"', '\\"')
    cmd = [
        'bash', '-c',
        f'export PATH="$HOME/.local/bin:$PATH" && uv run scripts/openalex_cli.py resolve works "{title_escaped}"'
    ]
    try:
        res = subprocess.run(cmd, cwd=openalex_dir, capture_output=True, text=True, check=True)
        candidates = json.loads(res.stdout)
        if candidates:
            # Pegar o primeiro candidato
            candidate = candidates[0]
            validation_results[key] = {
                'title': title,
                'doi': info['doi'],
                'status': f"Válido (Resolvido: {candidate.get('display_name')[:40]}...)",
                'openalex_id': candidate.get('id')
            }
        else:
            validation_results[key] = {
                'title': title,
                'doi': info['doi'],
                'status': "Suspeito: Não encontrado no OpenAlex",
                'openalex_id': ""
            }
    except Exception as e:
        validation_results[key] = {
            'title': title,
            'doi': info['doi'],
            'status': f"Erro na consulta: {e}",
            'openalex_id': ""
        }

# 4. Gerar Relatório Markdown
report_path = 'validation_report.md'
with open(report_path, 'w', encoding='utf-8') as f:
    f.write("# Relatório de Validação de Citações Científicas\n\n")
    f.write(f"Este relatório apresenta o resultado da validação das referências bibliográficas reais do artigo contra a base científica global **OpenAlex**.\n\n")
    
    total = len(cited_keys)
    validos = sum(1 for r in validation_results.values() if "Válido" in r['status'])
    suspeitos = total - validos
    
    f.write(f"## Resumo Geral\n")
    f.write(f"- **Total de Citações Únicas no Manuscrito:** {total}\n")
    f.write(f"- **Citações Validadas (Existentes no OpenAlex):** {validos}\n")
    f.write(f"- **Citações Suspeitas/Pendentes:** {suspeitos}\n\n")
    
    f.write("## Tabela Detalhada de Validação\n\n")
    f.write("| Chave | Título | Status no OpenAlex | ID OpenAlex |\n")
    f.write("| :--- | :--- | :--- | :--- |\n")
    
    for key, res in sorted(validation_results.items()):
        status_md = f"**{res['status']}**" if "Suspeito" in res['status'] or "ERRO" in res['status'] else res['status']
        openalex_link = f"[{res['openalex_id'].split('/')[-1]}]({res['openalex_id']})" if res['openalex_id'] else "-"
        f.write(f"| `{key}` | {res['title'][:80]}... | {status_md} | {openalex_link} |\n")

print(f"Relatório de validação salvo com sucesso em: {report_path}")
