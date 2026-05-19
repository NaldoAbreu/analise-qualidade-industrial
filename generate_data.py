import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime, timedelta

# Configurações
np.random.seed(42)
num_records = 1000
start_date = datetime(2024, 1, 1)

# 1. Gerar Produtos
produtos = pd.DataFrame({
    'id_produto': range(1, 11),
    'nome_produto': [f'Produto {chr(65+i)}' for i in range(10)],
    'custo_unitario_retrabalho': np.random.uniform(50, 200, 10).round(2)
})

# 2. Gerar Linhas de Produção
linhas = pd.DataFrame({
    'id_linha': range(1, 6),
    'nome_linha': [f'Linha {i}' for i in range(1, 6)]
})

# 3. Gerar Inspeções e Defeitos
def_types = ['Arranhão', 'Fissura', 'Dimensão Incorreta', 'Cor Fora do Padrão', 'Rebarba']
turnos = ['Manhã', 'Tarde', 'Noite']

data_inspecoes = []
for i in range(num_records):
    data_inspecao = start_date + timedelta(days=np.random.randint(0, 120), hours=np.random.randint(0, 24))
    id_produto = np.random.randint(1, 11)
    id_linha = np.random.randint(1, 6)
    turno = turnos[np.random.randint(0, 3)]
    
    # Simular taxa de defeito (ex: 15% de chance de defeito)
    tem_defeito = np.random.random() < 0.15
    tipo_defeito = np.random.choice(def_types) if tem_defeito else None
    
    data_inspecoes.append({
        'id_inspecao': i + 1,
        'data': data_inspecao,
        'id_produto': id_produto,
        'id_linha': id_linha,
        'turno': turno,
        'status': 'Defeituoso' if tem_defeito else 'OK',
        'tipo_defeito': tipo_defeito
    })

inspecoes = pd.DataFrame(data_inspecoes)

# Salvar em SQLite
conn = sqlite3.connect('/home/ubuntu/analise_qualidade_industrial/data/qualidade.db')
produtos.to_sql('produtos', conn, if_exists='replace', index=False)
linhas.to_sql('linhas', conn, if_exists='replace', index=False)
inspecoes.to_sql('inspecoes', conn, if_exists='replace', index=False)
conn.close()

print("Banco de dados SQLite criado com sucesso em /home/ubuntu/analise_qualidade_industrial/data/qualidade.db")
