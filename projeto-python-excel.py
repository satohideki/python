import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import os

arquivo = input('Caminho: ')
excel = (arquivo)
df = pd.read_excel(excel)
coluna = input('Qual coluna será a coluna? ')
linha = input('Qual coluna será a linha? ')
valor = input('Qual coluna será valores? ')

evento_group = df.groupby([linha, coluna]).mean()
print(evento_group[valor])



