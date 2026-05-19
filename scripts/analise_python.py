import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Criar diretório para salvar gráficos se não existir
os.makedirs('/home/ubuntu/analise_qualidade_industrial/outputs', exist_ok=True)

# Conectar ao banco
conn = sqlite3.connect('/home/ubuntu/analise_qualidade_industrial/data/qualidade.db')

# Carregar dados
df = pd.read_sql_query("SELECT * FROM inspecoes", conn)
df_produtos = pd.read_sql_query("SELECT * FROM produtos", conn)
df_linhas = pd.read_sql_query("SELECT * FROM linhas", conn)

# Merge para ter nomes das linhas e custos
df = df.merge(df_linhas, on='id_linha').merge(df_produtos, on='id_produto')
df['data'] = pd.to_datetime(df['data'])

# 1. Gráfico de tendência de defeitos ao longo do tempo
df_defeitos = df[df['status'] == 'Defeituoso'].copy()
df_defeitos['mes_ano'] = df_defeitos['data'].dt.to_period('M')
tendencia = df_defeitos.groupby('mes_ano').size()

plt.figure(figsize=(10, 6))
tendencia.plot(kind='line', marker='o', color='red')
plt.title('Tendência de Defeitos Mensais')
plt.xlabel('Mês/Ano')
plt.ylabel('Quantidade de Defeitos')
plt.grid(True)
plt.savefig('/home/ubuntu/analise_qualidade_industrial/outputs/tendencia_defeitos.png')
plt.close()

# 2. Pareto de tipos de defeito
pareto_data = df_defeitos['tipo_defeito'].value_counts().reset_index()
pareto_data.columns = ['tipo_defeito', 'contagem']
pareto_data['percent_acumulado'] = pareto_data['contagem'].cumsum() / pareto_data['contagem'].sum() * 100

fig, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(x='tipo_defeito', y='contagem', data=pareto_data, ax=ax1, palette='viridis')
ax2 = ax1.twinx()
ax2.plot(pareto_data['tipo_defeito'], pareto_data['percent_acumulado'], color='red', marker='D', ms=7)
ax2.set_ylim(0, 110)
plt.title('Pareto de Tipos de Defeito')
plt.savefig('/home/ubuntu/analise_qualidade_industrial/outputs/pareto_defeitos.png')
plt.close()

# 3. Heatmap de defeitos por turno x linha de produção
heatmap_data = df_defeitos.pivot_table(index='turno', columns='nome_linha', values='id_inspecao', aggfunc='count')

plt.figure(figsize=(10, 6))
sns.heatmap(heatmap_data, annot=True, cmap='YlOrRd', fmt='g')
plt.title('Heatmap: Defeitos por Turno e Linha')
plt.savefig('/home/ubuntu/analise_qualidade_industrial/outputs/heatmap_defeitos.png')
plt.close()

conn.close()
print("Análises concluídas e gráficos salvos em /home/ubuntu/analise_qualidade_industrial/outputs/")
