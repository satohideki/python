import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import os

csv = input ('Qual o caminho? ')
caminho = os.path.splitext(csv)[0]
df1 = pd.read_csv(csv)
separar = df1["SnapID;DataHora;Evento;Tempo(s)"].str.split(';')
dados = separar.to_list()
colunas = ['SnapID', 'DataHora', 'Evento', 'Tempo(s)']
df2 = pd.DataFrame(dados, columns = colunas)
evento_group = df2.groupby(['DataHora', 'Evento']).sum('Tempo(s)')
sort = evento_group.sort_values (by = 'Tempo(s)', ascending = False)
excel = sort.to_excel(caminho + '.xlsx')

