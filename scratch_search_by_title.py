import re
import glob

# Read bibliography
bib = open('latex/bibliography.bib', 'r', encoding='utf-8').read()

# Extract titles: title = {The title} or title = "The title"
# This regex is simple but effective for standard bibtex
titles_raw = re.findall(r'title\s*=\s*[\{"](.*?)(?:[\}"]\s*,|[\}"]\s*\n)', bib, re.DOTALL | re.IGNORECASE)

# Clean titles
titles = []
for t in titles_raw:
    clean_t = re.sub(r'[\{\}\n]', ' ', t).strip()
    clean_t = re.sub(r'\s+', ' ', clean_t)
    titles.append(clean_t)

# Print a few to test
print(f"Encontramos {len(titles)} títulos no arquivo.")
print("Exemplos:", titles[:5])
