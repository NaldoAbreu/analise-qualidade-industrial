import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime, timedelta

# Settings
np.random.seed(42)
num_records = 1000
start_date = datetime(2024, 1, 1)

# 1. Generate Products
products = pd.DataFrame({
    'product_id': range(1, 11),
    'product_name': [f'Product {chr(65+i)}' for i in range(10)],
    'unit_rework_cost': np.random.uniform(50, 200, 10).round(2)
})

# 2. Generate Production Lines
lines = pd.DataFrame({
    'line_id': range(1, 6),
    'line_name': [f'Line {i}' for i in range(1, 6)]
})

# 3. Generate Inspections and Defects
def_types = ['Scratch', 'Crack', 'Incorrect Dimension', 'Color Off-Standard', 'Burr']
shifts = ['Morning', 'Afternoon', 'Night']

inspection_data = []
for i in range(num_records):
    inspection_date = start_date + timedelta(days=np.random.randint(0, 120), hours=np.random.randint(0, 24))
    product_id = np.random.randint(1, 11)
    line_id = np.random.randint(1, 6)
    shift = shifts[np.random.randint(0, 3)]
    
    # Simulate defect rate (e.g., 15% chance of defect)
    has_defect = np.random.random() < 0.15
    defect_type = np.random.choice(def_types) if has_defect else None
    
    inspection_data.append({
        'inspection_id': i + 1,
        'date': inspection_date,
        'product_id': product_id,
        'line_id': line_id,
        'shift': shift,
        'status': 'Defective' if has_defect else 'OK',
        'defect_type': defect_type
    })

inspections = pd.DataFrame(inspection_data)

# Save to SQLite
conn = sqlite3.connect('/home/ubuntu/analise_qualidade_industrial/data/quality.db')
products.to_sql('products', conn, if_exists='replace', index=False)
lines.to_sql('lines', conn, if_exists='replace', index=False)
inspections.to_sql('inspections', conn, if_exists='replace', index=False)
conn.close()

print("SQLite database successfully created at /home/ubuntu/analise_qualidade_industrial/data/quality.db")
