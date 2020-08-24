import csv
import requests
from config import URL, ARQUIVO_CSV
import pandas as pd

# requisição para o link para o arquivo.csv
response = requests.get(URL)
# print(response.content)

# criando um arquivo chamado covid-19.csv e salvando no pc local
with open('covid19.csv', 'w', newline='\n') as nome_arquivo:
    writer = csv.writer(nome_arquivo)
    for linha in response.iter_lines():
        writer.writerow(linha.decode('utf-8').split(','))

# Abrir um arquivo .csv a partir do projeto raiz
with open(ARQUIVO_CSV) as arquivo:
    leitor_exemplo = csv.reader(arquivo)
    for linha in leitor_exemplo:
        # print(linha)
        if linha[2] == "Brazil":
            print(f"Linha # {leitor_exemplo.line_num} {linha}")

# Usando o módulo pandas para ler um arquivo csv
arquivo_csv = pd.read_csv(ARQUIVO_CSV, usecols=['location', 'date', 'total_cases', 'new_cases', 'total_deaths'], index_col='date')

# Mostrando os 10 primeiros
print(arquivo_csv.head().to_string())

# Filtrando os dados
print(arquivo_csv.loc[(arquivo_csv.location == 'Italy') & (arquivo_csv.index == '2020-08-12')])

