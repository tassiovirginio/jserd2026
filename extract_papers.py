import re
import os
import json

def main():
    # 1. Obter citações usadas no main.aux
    try:
        with open('latex/main.aux', 'r') as f:
            aux_content = f.read()
    except FileNotFoundError:
        print("Erro: main.aux não encontrado. Compile o projeto latex primeiro.")
        return

    cites = re.findall(r'\\citation\{([^}]+)\}', aux_content)
    keys = set()
    for c in cites:
        for k in c.split(','):
            keys.add(k.strip())
    
    print(f"Foram encontradas {len(keys)} citações únicas no main.aux")

    # 2. Ler o bibliography.bib com regex
    try:
        with open('latex/bibliography.bib', 'r', encoding='utf-8') as f:
            bib_content = f.read()
    except Exception as e:
        print(f"Erro ao ler bibliography.bib: {e}")
        return

    entries = {}
    # Busca por blocos do tipo @article{chave, ... } ou @inproceedings{chave, ... }
    # A regex a seguir tenta pegar as chaves e o conteúdo até o próximo @
    parts = re.split(r'\n@', bib_content)
    for part in parts:
        if not part.strip():
            continue
        # Pega a chave: tudo antes da primeira vírgula (depois do {)
        match_key = re.search(r'^[^{]+\{([^,]+),', part)
        if match_key:
            key = match_key.group(1).strip()
            
            # Extrair DOI
            doi_match = re.search(r'doi\s*=\s*[\{"]([^}"]+)[\}"]', part, re.IGNORECASE)
            doi = doi_match.group(1) if doi_match else None
            
            # Extrair URL
            url_match = re.search(r'url\s*=\s*[\{"]([^}"]+)[\}"]', part, re.IGNORECASE)
            url = url_match.group(1) if url_match else None
            
            # Extrair Título
            title_match = re.search(r'title\s*=\s*[\{"]([^}"]+)[\}"]', part, re.IGNORECASE)
            title = title_match.group(1) if title_match else None
            
            entries[key] = {
                "ID": key,
                "doi": doi,
                "url": url,
                "title": title
            }

    to_download = []
    for key in keys:
        if key in entries:
            to_download.append(entries[key])
        else:
            print(f"Aviso: Chave '{key}' não encontrada no bibliography.bib")

    # 3. Salvar os metadados extraídos
    with open('papers_to_download.json', 'w', encoding='utf-8') as f:
        json.dump(to_download, f, indent=2, ensure_ascii=False)

    print(f"Metadados de {len(to_download)} artigos salvos em 'papers_to_download.json'.")
    
    # 4. Mostrar alguns exemplos do que encontramos
    print("\nResumo das entradas para download:")
    for i, p in enumerate(to_download[:5]):
        doi = p.get('doi') or 'Sem DOI'
        url = p.get('url') or 'Sem URL'
        print(f" - {p.get('ID')}: DOI={doi}, URL={url}")
    print("...")

if __name__ == '__main__':
    main()
