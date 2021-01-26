import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import os

arquivo = input('Caminho: ')



excel_file = (r'C:\Users\bruno.sato\my-first-project\python\awrtimebreakdown102.xlsx')
df = pd.read_excel(excel_file)
evento_group = df.groupby(['DataHora', 'Evento']).mean()
print(evento_group['Tempo(s)'])



