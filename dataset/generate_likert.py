import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import nbformat as nbf

# 1. Prepare data (we will also put this code inside the Jupyter Notebook)
code_cells = []

cell_1 = """# Análise de Sentimentos: Gráfico Estilo Likert (Diverging Stacked Bar Chart)
#
# Este notebook extrai a contagem de sentimentos negativos, neutros e positivos
# do banco de dados `resultado.sqlite` e plota um gráfico de barras empilhadas divergente,
# comparando o "Overview Geral" com cada tipo de Test Smell.

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Caminho do banco de dados
db_path = '/home/tassio/.dnose/results/resultado.sqlite'

# Conectando ao banco de dados
conn = sqlite3.connect(db_path)

# Função auxiliar para pegar as contagens
def get_counts(query):
    return pd.read_sql_query(query, conn)

# 1. Buscando o Overview Geral (Baseline)
query_geral = '''
SELECT 
    SUM(CASE WHEN score < 0 THEN 1 ELSE 0 END) as Negative,
    SUM(CASE WHEN score = 0 THEN 1 ELSE 0 END) as Neutral,
    SUM(CASE WHEN score > 0 THEN 1 ELSE 0 END) as Positive
FROM commit_sentiments
WHERE score IS NOT NULL
'''
df_geral = get_counts(query_geral)
df_geral['Category'] = 'Overview Geral (Baseline)'

# 2. Buscando as contagens por tipo de Test Smell
# Como um commit pode ter múltiplos smells do mesmo tipo, usamos COUNT(DISTINCT c.hash)
query_smells = '''
SELECT 
    t.testsmell as Category,
    COUNT(DISTINCT CASE WHEN c.score < 0 THEN c.hash END) as Negative,
    COUNT(DISTINCT CASE WHEN c.score = 0 THEN c.hash END) as Neutral,
    COUNT(DISTINCT CASE WHEN c.score > 0 THEN c.hash END) as Positive
FROM commit_sentiments c
JOIN testsmells t ON c.hash = t."commit"
WHERE c.score IS NOT NULL
GROUP BY t.testsmell
'''
df_smells = get_counts(query_smells)

# Fechando a conexão
conn.close()

# Concatenando os dataframes
df = pd.concat([df_geral, df_smells], ignore_index=True)

# Calculando o total e as porcentagens para cada linha
df['Total'] = df['Negative'] + df['Neutral'] + df['Positive']
df['Neg_Pct'] = (df['Negative'] / df['Total']) * 100
df['Neu_Pct'] = (df['Neutral'] / df['Total']) * 100
df['Pos_Pct'] = (df['Positive'] / df['Total']) * 100

# Ordenando o dataframe para o gráfico ficar bonito:
# Vamos fixar o Overview Geral no topo, e ordenar o resto pelo percentual de negativo
df_baseline = df[df['Category'] == 'Overview Geral (Baseline)']
df_rest = df[df['Category'] != 'Overview Geral (Baseline)'].sort_values('Neg_Pct', ascending=True)
df_final = pd.concat([df_rest, df_baseline], ignore_index=True)

df_final
"""
code_cells.append(cell_1)

cell_2 = """# Configurando e gerando o gráfico divergente (Likert Scale)
# Para centralizar a barra neutra no zero:
# A barra negativa começa em: -(Neg_Pct + Neu_Pct/2)
# A barra neutra começa em: -(Neu_Pct/2)
# A barra positiva começa em: (Neu_Pct/2)

fig, ax = plt.subplots(figsize=(14, 10))

categories = df_final['Category']
y_pos = np.arange(len(categories))

# Calculando os pontos de início para cada barra
starts_neg = -(df_final['Neg_Pct'] + df_final['Neu_Pct'] / 2)
starts_neu = -(df_final['Neu_Pct'] / 2)
starts_pos = (df_final['Neu_Pct'] / 2)

# Cores
color_neg = '#d7191c' # Vermelho
color_neu = '#cccccc' # Cinza
color_pos = '#2c7bb6' # Azul

# Plotando as barras
ax.barh(y_pos, df_final['Neg_Pct'], left=starts_neg, height=0.6, color=color_neg, label='Negativo (< 0)')
ax.barh(y_pos, df_final['Neu_Pct'], left=starts_neu, height=0.6, color=color_neu, label='Neutro (0)')
ax.barh(y_pos, df_final['Pos_Pct'], left=starts_pos, height=0.6, color=color_pos, label='Positivo (> 0)')

# Adicionando rótulos de porcentagem dentro das barras
for i in range(len(y_pos)):
    neg_val = df_final['Neg_Pct'].iloc[i]
    neu_val = df_final['Neu_Pct'].iloc[i]
    pos_val = df_final['Pos_Pct'].iloc[i]
    
    # Texto negativo
    if neg_val > 2: # Só mostra se for maior que 2% para não ficar espremido
        ax.text(starts_neg[i] + neg_val/2, y_pos[i], f'{neg_val:.1f}%', va='center', ha='center', color='white', fontweight='bold')
    
    # Texto neutro
    if neu_val > 5:
        ax.text(starts_neu[i] + neu_val/2, y_pos[i], f'{neu_val:.1f}%', va='center', ha='center', color='black')
        
    # Texto positivo
    if pos_val > 2:
        ax.text(starts_pos[i] + pos_val/2, y_pos[i], f'{pos_val:.1f}%', va='center', ha='center', color='white', fontweight='bold')

# Configurações do gráfico
ax.set_yticks(y_pos)
ax.set_yticklabels(categories, fontsize=12)
ax.set_xlabel('Porcentagem de Commits (%)', fontsize=12)
ax.set_title('Distribuição de Sentimentos: Overview Geral vs Tipos de Test Smells', fontsize=16, pad=20)

# Destacar a linha de Base (Overview Geral)
ax.get_yticklabels()[-1].set_fontweight("bold")

# Linha do zero
ax.axvline(0, color='black', linewidth=1.5, linestyle='--')

# Ajustando o limite X
max_val = max(abs(starts_neg.min()), (starts_pos + df_final['Pos_Pct']).max()) + 5
ax.set_xlim(-max_val, max_val)

# Customizando as labels do eixo X para mostrar valores positivos em ambos os lados
ticks = ax.get_xticks()
ax.set_xticklabels([f'{abs(int(tick))}%' for tick in ticks])

# Legenda
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.08), ncol=3, fontsize=12)

plt.tight_layout()

# Salvando a imagem na mesma pasta
output_path = '/home/tassio/Development/pessoal/jserd2026/dataset/sentiment_likert_chart.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.show()

print(f'Gráfico salvo com sucesso em: {output_path}')
"""
code_cells.append(cell_2)

# Create the Jupyter Notebook
nb = nbf.v4.new_notebook()
cells = []

# Add intro markdown
intro = """# Análise de Sentimentos em Commits (Estilo Escala Likert)
Este notebook foi gerado para responder a questão sobre a proporção de sentimentos **Negativos**, **Neutros** e **Positivos** no projeto geral versus cada tipo específico de *test smell*.

Foi utilizado o gráfico de barras empilhadas divergente, onde a barra neutra fica centralizada no eixo 0, permitindo fácil comparação visual do peso negativo vs positivo de cada categoria.
"""
cells.append(nbf.v4.new_markdown_cell(intro))

# Add code cells
for code in code_cells:
    cells.append(nbf.v4.new_code_cell(code))

nb['cells'] = cells

with open('/home/tassio/Development/pessoal/jserd2026/dataset/likert_sentiments_analysis.ipynb', 'w') as f:
    nbf.write(nb, f)

print("Jupyter Notebook 'likert_sentiments_analysis.ipynb' gerado com sucesso!")

# Now execute the python code directly to generate the image
exec(cell_1)
exec(cell_2)
