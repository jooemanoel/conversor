import json
import pandas as pd

# Carregar o arquivo Excel
df = pd.read_excel("produtos.xlsx")
# Converter o DataFrame em um dicionário
dados = df.to_dict(orient='records')
print(dados)
# Salvar o dicionário como JSON com caracteres legíveis
with open('produtos.json', 'w', encoding='utf-8') as json_file:
    json.dump(dados, json_file, ensure_ascii=False, indent=4)
