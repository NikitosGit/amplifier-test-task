import pandas as pd
import requests

xlsx_file = 'example.xlsx'
df = pd.read_excel(xlsx_file)

column_names = df.columns.tolist()
# print(column_names)
api_data = []

for index, row in df.iterrows():
    row_data = {}
    for i, column in enumerate(column_names):
        row_data[column] = row[i]

    api_data.append(row_data)

api_url = 'http://localhost:8000/materials/'

headers = {
    'Content-Type': 'application/json'
}

for data in api_data:
    response = requests.post(api_url, headers=headers, json=data)

    if response.status_code == 201:
        print(f'Row created successfully: {data}')
    else:
        print(f'Error creating row: {response.text}')
