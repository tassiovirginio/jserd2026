import pandas as pd
import matplotlib.pyplot as plt

# Configuração do estilo
plt.rcParams['figure.figsize'] = (14, 8)
plt.rcParams['font.size'] = 10

# ============================================
# Gráfico 1: Top 20 Autores por Quantidade de Projetos
# ============================================
df_projects = pd.read_csv("authors_projects.csv")
df_top20_projects = df_projects.head(20)

fig, ax = plt.subplots()
bars = ax.barh(df_top20_projects['author'], df_top20_projects['quantidade'], color='steelblue')
ax.set_xlabel('Quantidade de Projetos Distintos')
ax.set_ylabel('Autor')
ax.set_title('Top 20 Autores por Quantidade de Projetos Distintos')
ax.invert_yaxis()  # Maior no topo
plt.tight_layout()
plt.savefig('authors_projects_chart.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ Salvo: authors_projects_chart.png")

# ============================================
# Gráfico 2: Top 20 Autores - Soma de Sentimentos Negativos
# ============================================
df_sum = pd.read_csv("authors_negative_sentiment_sum.csv")
df_top20_sum = df_sum.head(20)

fig, ax = plt.subplots()
colors = ['#d62728' if x < -1000 else '#ff7f0e' if x < -500 else '#ffbb78' for x in df_top20_sum['total_score']]
bars = ax.barh(df_top20_sum['author'], df_top20_sum['total_score'], color=colors)
ax.set_xlabel('Soma Total de Sentimentos Negativos')
ax.set_ylabel('Autor')
ax.set_title('Top 20 Autores com Maior Soma de Sentimentos Negativos')
ax.invert_yaxis()
ax.axvline(x=0, color='black', linewidth=0.5)
plt.tight_layout()
plt.savefig('authors_negative_sum_chart.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ Salvo: authors_negative_sum_chart.png")

# ============================================
# Gráfico 3: Top 20 Autores - Média de Sentimentos Negativos
# ============================================
df_avg = pd.read_csv("authors_negative_sentiment_avg.csv")
df_top20_avg = df_avg.head(20)

fig, ax = plt.subplots()
colors = ['#d62728' if x < -4 else '#ff7f0e' if x < -3 else '#ffbb78' for x in df_top20_avg['media']]
bars = ax.barh(df_top20_avg['author'], df_top20_avg['media'], color=colors)
ax.set_xlabel('Média de Sentimentos Negativos')
ax.set_ylabel('Autor')
ax.set_title('Top 20 Autores com Maior Média de Sentimentos Negativos')
ax.invert_yaxis()
ax.axvline(x=0, color='black', linewidth=0.5)
plt.tight_layout()
plt.savefig('authors_negative_avg_chart.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ Salvo: authors_negative_avg_chart.png")

# ============================================
# Gráfico 4: Comparativo - Projetos vs Soma Negativos (scatter)
# ============================================
df_merged = pd.merge(df_projects, df_sum, on='author', how='inner')

fig, ax = plt.subplots()
scatter = ax.scatter(df_merged['quantidade'], df_merged['total_score'], 
                     alpha=0.6, c=df_merged['total_score'], cmap='RdYlGn', s=50)
ax.set_xlabel('Quantidade de Projetos Distintos')
ax.set_ylabel('Soma de Sentimentos Negativos')
ax.set_title('Relação: Quantidade de Projetos vs Sentimentos Negativos por Autor')
ax.axhline(y=0, color='gray', linestyle='--', linewidth=0.5)
plt.colorbar(scatter, label='Total Score')
plt.tight_layout()
plt.savefig('authors_projects_vs_sentiment_scatter.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ Salvo: authors_projects_vs_sentiment_scatter.png")

print("\n🎉 Todos os gráficos foram gerados com sucesso!")
