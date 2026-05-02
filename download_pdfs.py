import json
import os
import time
import requests
import urllib.parse

def main():
    if not os.path.exists('pdfs'):
        os.makedirs('pdfs')

    try:
        with open('papers_to_download.json', 'r', encoding='utf-8') as f:
            papers = json.load(f)
    except Exception as e:
        print(f"Erro ao ler papers_to_download.json: {e}")
        return

    email = "tassio.virginio@ifto.edu.br"
    downloaded_count = 0

    print(f"Iniciando tentativa de download de {len(papers)} artigos...")

    for paper in papers:
        pid = paper.get('ID')
        doi = paper.get('doi')
        
        if not doi:
            print(f"[{pid}] Sem DOI, ignorando download automático.")
            continue
            
        # Clean up DOI
        doi = doi.replace('\\', '').strip()
        if doi.startswith('http'):
            # try to extract doi from url
            if 'doi.org/' in doi:
                doi = doi.split('doi.org/')[-1]
            else:
                print(f"[{pid}] DOI em formato não reconhecido: {doi}")
                continue

        pdf_path = os.path.join('pdfs', f"{pid}.pdf")
        if os.path.exists(pdf_path):
            print(f"[{pid}] Já baixado: {pdf_path}")
            downloaded_count += 1
            continue

        print(f"[{pid}] Buscando PDF open access via Unpaywall (DOI: {doi})...")
        
        # Consultar Unpaywall
        unpaywall_url = f"https://api.unpaywall.org/v2/{doi}?email={email}"
        try:
            resp = requests.get(unpaywall_url, timeout=10)
            if resp.status_code == 200:
                data = resp.json()
                if data.get('is_oa') and data.get('best_oa_location') and data['best_oa_location'].get('url_for_pdf'):
                    pdf_url = data['best_oa_location']['url_for_pdf']
                    print(f"[{pid}] Encontrado PDF: {pdf_url}. Baixando...")
                    
                    pdf_resp = requests.get(pdf_url, stream=True, timeout=15)
                    if pdf_resp.status_code == 200 and 'pdf' in pdf_resp.headers.get('Content-Type', '').lower():
                        with open(pdf_path, 'wb') as pdf_file:
                            for chunk in pdf_resp.iter_content(chunk_size=8192):
                                pdf_file.write(chunk)
                        print(f"[{pid}] Download concluído com sucesso!")
                        downloaded_count += 1
                    else:
                        print(f"[{pid}] Falha ao baixar o PDF direto (Status: {pdf_resp.status_code}).")
                else:
                    print(f"[{pid}] Nenhum PDF Open Access disponível.")
            else:
                print(f"[{pid}] Erro ao consultar Unpaywall: {resp.status_code}")
        except Exception as e:
            print(f"[{pid}] Erro na requisição: {e}")
            
        # Esperar 1s para não sobrecarregar as APIs
        time.sleep(1)

    print(f"\nFinalizado! {downloaded_count} PDFs disponíveis na pasta 'pdfs/'.")

if __name__ == '__main__':
    main()
