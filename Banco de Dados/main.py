# Abir os arquivos Excel

# Para cada arquivo, verificar se há algum valor maior que R$55.000,00 em vendas

# Se for maior que R$55.000,00 será enviado um SMS como o Nome, Vendas e Mês

# INSTALAR AS SEGUINTES BIBLIOTECAS:
    # pandas,
    # openpyxl (integração com o Excel) e
    # twilio (integração com o SMS)

import pandas as pd

from twilio.rest import Client
# "ZF6EE2PPS8P6MLX9PAD15EW6"
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "1bXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    # Se alguém dentro da tabaela 'Vendas' for maior que 55000, tem que usar any() para ver individualmente
    if (tabela_vendas['Vendas'] > 55000).any():
        # Minha linha é baseada na condição de Vendas > 55000
        vendedor = tabela_vendas.loc[(tabela_vendas['Vendas'] > 55000), 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[(tabela_vendas['Vendas'] > 55000), 'Vendas'].values[0]
        message = client.messages.create(
            to='+55552299XXXXXXX',  # Exemplo: +55 (55) 2299-8787
            from_="+XXXXXXXXXXX", # My Twilio phone number
            body=f'No mês de {mes} alguém bateu a meta. Vendedor {vendedor}. Vendas {vendas}.'
        )
        print(message.sid) # Código para confirmar o envio da mensagem