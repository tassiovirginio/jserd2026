import re
import json

bib_content = open('latex/bibliography.bib', 'r', encoding='utf-8').read()

# match doi = {10.xxx} or doi = "10.xxx"
doi_matches = re.findall(r'doi\s*=\s*[\{"](10\.\d{4,9}/[-._;()/:A-Za-z0-9]+)[\}"]', bib_content)
# match https://doi.org/10.xxx
url_matches = re.findall(r'https?://doi\.org/(10\.\d{4,9}/[-._;()/:A-Za-z0-9]+)', bib_content)

dois = list(set(doi_matches + url_matches))
print(json.dumps(dois))
