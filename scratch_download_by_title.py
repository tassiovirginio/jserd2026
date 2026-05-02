import re
import os
import time
import requests
import urllib.parse

bib = open('latex/bibliography.bib', 'r', encoding='utf-8').read()
titles_raw = re.findall(r'^\s*title\s*=\s*[\{"](.*?)(?:[\}"]\s*,|[\}"]\s*\n)', bib, re.MULTILINE | re.IGNORECASE)

titles = []
for t in titles_raw:
    clean_t = re.sub(r'[\{\}\n]', ' ', t).strip()
    clean_t = re.sub(r'\s+', ' ', clean_t)
    titles.append(clean_t)

out_dir = 'artigos'
if not os.path.exists(out_dir):
    os.makedirs(out_dir)

existing_files = os.listdir(out_dir)

def clean_filename(t):
    return re.sub(r'[^a-zA-Z0-9]+', '_', t)

print(f"Tentando baixar {len(titles)} artigos pelo titulo...")
downloaded = 0
for t in titles:
    fname = clean_filename(t)
    # Check if already downloaded (approximate name match)
    found = False
    for ef in existing_files:
        if fname[:20].lower() in ef.lower():
            found = True
            break
    if found:
        continue
    
    print(f"Buscando: {t[:50]}...")
    try:
        url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={urllib.parse.quote(t)}&limit=1&fields=title,openAccessPdf"
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            if data.get('data') and len(data['data']) > 0:
                paper = data['data'][0]
                oa = paper.get('openAccessPdf')
                if oa and oa.get('url'):
                    pdf_url = oa['url']
                    print(f"  -> Encontrado PDF: {pdf_url}")
                    pdf_resp = requests.get(pdf_url, stream=True, timeout=15)
                    if pdf_resp.status_code == 200:
                        pdf_path = os.path.join(out_dir, f"{fname[:100]}.pdf")
                        with open(pdf_path, 'wb') as f:
                            for chunk in pdf_resp.iter_content(chunk_size=8192):
                                f.write(chunk)
                        print("  -> Sucesso!")
                        downloaded += 1
                    else:
                        print(f"  -> Erro ao baixar PDF ({pdf_resp.status_code})")
                else:
                    print("  -> Sem PDF Open Access.")
            else:
                print("  -> Não encontrado no Semantic Scholar.")
        else:
            print(f"  -> Erro na API ({resp.status_code})")
    except Exception as e:
        print(f"  -> Exceção: {e}")
    
    time.sleep(1) # rate limit

print(f"Foram baixados {downloaded} novos PDFs.")
