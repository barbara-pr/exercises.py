import pandas as pd

# Codicações para ser compatível com CSV
tabela1 = pd.read_csv('tabela-exemplo.csv', encoding='latin1')  # or 'iso-8859-1' or 'cp1252'
print(tabela1)

print('-' * 20)

tabela2 = pd.read_excel('tabela-exemplo.xlsx')
print(tabela2)