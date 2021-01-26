import pandas as pd

excel_file = (r'C:\Users\bruno.sato\my-first-project\python\awrtimebreakdown102.xlsx')
df = pd.read_excel(excel_file)
print (df.loc[:,'CPU'])

