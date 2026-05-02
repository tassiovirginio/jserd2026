import os
import re
import glob

# 1. Obter todas as chaves de citação usadas nos arquivos .tex
tex_files = glob.glob('latex/**/*.tex', recursive=True)
cited_keys = set()
for tf in tex_files:
    try:
        content = open(tf, 'r', encoding='utf-8').read()
        # Procura por \cite{key1, key2}, \citep{...}, \citet{...} etc
        cites = re.findall(r'\\cite[a-zA-Z]*\*?\{([^}]+)\}', content)
        for cite in cites:
            keys = [k.strip() for k in cite.split(',')]
            cited_keys.update(keys)
    except Exception as e:
        pass

# 2. Ler o bibliography.bib e mapear chaves para títulos
bib_content = open('latex/bibliography.bib', 'r', encoding='utf-8').read()
entries = bib_content.split('@')

bib_map = {} # key -> title
for entry in entries:
    if not entry.strip(): continue
    # ex: inproceedings{guzman2014,
    match_key = re.search(r'^[a-zA-Z]+\s*\{([^,]+),', entry)
    if match_key:
        key = match_key.group(1).strip()
        # extract title
        match_title = re.search(r'title\s*=\s*[\{"](.*?)(?:[\}"]\s*,|[\}"]\s*\n)', entry, re.IGNORECASE | re.DOTALL)
        if match_title:
            t = match_title.group(1)
            clean_t = re.sub(r'[\{\}\n]', ' ', t).strip()
            clean_t = re.sub(r'\s+', ' ', clean_t)
            bib_map[key] = clean_t

# 3. Verificar arquivos na pasta artigos/
downloaded_files = os.listdir('artigos')

def clean_filename(t):
    return re.sub(r'[^a-zA-Z0-9]+', '_', t)

downloaded_list = []
missing_list = []

for key in cited_keys:
    if key in bib_map:
        title = bib_map[key]
        fname = clean_filename(title)[:20].lower()
        
        found = False
        for df in downloaded_files:
            if fname in df.lower():
                found = True
                break
        
        if found:
            downloaded_list.append((key, title))
        else:
            missing_list.append((key, title))
    else:
        # Cited but not in bibliography (or couldn't parse title)
        missing_list.append((key, "[Título não encontrado no .bib]"))

print(f"=== RESULTADO ===")
print(f"Total de citações únicas no texto: {len(cited_keys)}")
print(f"Total Baixados (Usados no Artigo): {len(downloaded_list)}")
print(f"Total Faltando (Usados no Artigo): {len(missing_list)}")

print("\n--- BAIXADOS ---")
for k, t in sorted(downloaded_list, key=lambda x: x[0]):
    print(f"[{k}] {t[:70]}...")

print("\n--- FALTANDO ---")
for k, t in sorted(missing_list, key=lambda x: x[0]):
    print(f"[{k}] {t[:70]}...")

