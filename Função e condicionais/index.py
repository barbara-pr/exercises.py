# definindo uma função com operadores e condicionais
def calcular_desconto(valor):
    if valor < 2500:
        desconto = 0
    elif valor < 6000:
        desconto = 0.04
    elif valor < 10000:
        desconto = 0.07
    else:
        desconto = 0.11
    return desconto  # retornar o valor do desconto após as verificações

# definindo as variáveis e respectivos cálculos
def calcular_valor_com_desconto(valor, quantidade):
    desconto = calcular_desconto(valor)
    valor_total_sem_desconto = valor * quantidade
    valor_desconto = valor_total_sem_desconto * desconto
    valor_total_com_desconto = valor_total_sem_desconto - valor_desconto
    return valor_total_sem_desconto, valor_total_com_desconto

print('Bem-vindo à Loja da Bárbara')
valor = float(input('Digite o valor do produto: '))
quantidade = int(input('Digite a quantidade do produto: '))

valor_total_sem_desconto, valor_com_desconto = calcular_valor_com_desconto(valor, quantidade)

# formatar os resultados com duas casas decimais
print(f'O valor SEM desconto é R$ {valor_total_sem_desconto:.2f}')
print(f'O valor COM desconto é R$ {valor_com_desconto:.2f}')
