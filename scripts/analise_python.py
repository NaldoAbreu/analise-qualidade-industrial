import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create directory for saving charts if it doesn't exist
os.makedirs('/home/ubuntu/analise_qualidade_industrial/outputs', exist_ok=True)

# Connect to database
conn = sqlite3.connect('/home/ubuntu/analise_qualidade_industrial/data/quality.db')

# Load data
df = pd.read_sql_query("SELECT * FROM inspections", conn)
df_products = pd.read_sql_query("SELECT * FROM products", conn)
df_lines = pd.read_sql_query("SELECT * FROM lines", conn)

# Merge to get line names and costs
df = df.merge(df_lines, on='line_id').merge(df_products, on='product_id')
df['date'] = pd.to_datetime(df['date'])

# 1. Defect trend chart over time
df_defects = df[df['status'] == 'Defective'].copy()
df_defects['month_year'] = df_defects['date'].dt.to_period('M')
trend = df_defects.groupby('month_year').size()

plt.figure(figsize=(10, 6))
trend.plot(kind='line', marker='o', color='red')
plt.title('Monthly Defect Trend')
plt.xlabel('Month/Year')
plt.ylabel('Number of Defects')
plt.grid(True)
plt.savefig('/home/ubuntu/analise_qualidade_industrial/outputs/tendencia_defeitos.png')
plt.close()

# 2. Pareto of defect types
pareto_data = df_defects['defect_type'].value_counts().reset_index()
pareto_data.columns = ['defect_type', 'count']
pareto_data['cumulative_percent'] = pareto_data['count'].cumsum() / pareto_data['count'].sum() * 100

fig, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(x='defect_type', y='count', data=pareto_data, ax=ax1, palette='viridis')
ax2 = ax1.twinx()
ax2.plot(pareto_data['defect_type'], pareto_data['cumulative_percent'], color='red', marker='D', ms=7)
ax2.set_ylim(0, 110)
plt.title('Pareto Chart of Defect Types')
plt.savefig('/home/ubuntu/analise_qualidade_industrial/outputs/pareto_defeitos.png')
plt.close()

# 3. Heatmap of defects by shift x production line
heatmap_data = df_defects.pivot_table(index='shift', columns='line_name', values='inspection_id', aggfunc='count')

plt.figure(figsize=(10, 6))
sns.heatmap(heatmap_data, annot=True, cmap='YlOrRd', fmt='g')
plt.title('Heatmap: Defects by Shift and Line')
plt.savefig('/home/ubuntu/analise_qualidade_industrial/outputs/heatmap_defeitos.png')
plt.close()

conn.close()
print("Analysis completed and charts saved in /home/ubuntu/analise_qualidade_industrial/outputs/")
