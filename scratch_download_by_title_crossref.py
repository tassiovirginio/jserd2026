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
existing_files = os.listdir(out_dir)

def clean_filename(t):
    return re.sub(r'[^a-zA-Z0-9]+', '_', t)

print(f"Tentando baixar artigos pelo titulo via CrossRef -> Unpaywall...")
downloaded = 0
email = "tassio.virginio@ifto.edu.br"

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
    
    print(f"Buscando DOI para: {t[:50]}...")
    try:
        # 1. Obter DOI via CrossRef usando o título
        cr_url = f"https://api.crossref.org/works?query.title={urllib.parse.quote(t)}&select=DOI,title&rows=1&mailto={email}"
        resp_cr = requests.get(cr_url, timeout=10)
        
        doi = None
        if resp_cr.status_code == 200:
            cr_data = resp_cr.json()
            items = cr_data.get('message', {}).get('items', [])
            if items:
                doi = items[0].get('DOI')
                
        if doi:
            # 2. Obter PDF via Unpaywall
            unp_url = f"https://api.unpaywall.org/v2/{doi}?email={email}"
            resp_unp = requests.get(unp_url, timeout=10)
            if resp_unp.status_code == 200:
                data = resp_unp.json()
                if data.get('is_oa') and data.get('best_oa_location') and data['best_oa_location'].get('url_for_pdf'):
                    pdf_url = data['best_oa_location']['url_for_pdf']
                    print(f"  -> Encontrado PDF: {pdf_url}")
                    
                    pdf_resp = requests.get(pdf_url, stream=True, timeout=15)
                    if pdf_resp.status_code == 200 and 'pdf' in pdf_resp.headers.get('Content-Type', '').lower():
                        pdf_path = os.path.join(out_dir, f"{fname[:100]}.pdf")
                        with open(pdf_path, 'wb') as f:
                            for chunk in pdf_resp.iter_content(chunk_size=8192):
                                f.write(chunk)
                        print("  -> Sucesso!")
                        downloaded += 1
                        existing_files.append(f"{fname[:100]}.pdf") # prevent retrying
                    else:
                        print(f"  -> Falha no download do PDF ({pdf_resp.status_code})")
                else:
                    print("  -> Sem PDF Open Access no Unpaywall.")
            else:
                print(f"  -> Erro Unpaywall ({resp_unp.status_code})")
        else:
            print("  -> DOI não encontrado no CrossRef.")
            
    except Exception as e:
        print(f"  -> Exceção: {e}")
    
    time.sleep(1) # rate limit

print(f"Foram baixados {downloaded} novos PDFs.")
