def escolha_servico():
    while True:
        servico = input('Entre com o tipo de serviço desejado (DIG/ICO/IPB/FOT): ').upper()
        if servico in ['DIG', 'ICO', 'IPB', 'FOT']:
            return servico
        else:
            print('Escolha inválida, entre com o tipo do serviço novamente.')


def num_paginas():
    while True:
        try:
            paginas = int(input('Entre com o número de páginas: ')) #sem o 'int' retorna uma string
            if paginas < 20:
                return paginas
            elif paginas < 200:
                return paginas * 0.85    #desconto de 15%
            elif paginas < 2000:
                return paginas * 0.80    #desconto de 20%
            elif paginas < 20000:
                return paginas * 0.75    #desconto de 25%
            else:
                print('Não aceitamos tantas páginas de uma vez. Por favor, entre com o número de páginas novamente.')
        except ValueError:
            print('Valor inválido. Por favor, entre com um valor numérico.')


def servico_extra():
    while True:
        try:
            servico_extra = int(input('Deseja algum serviço extra? (Encadernação Simples: 1 / Encadernação Capa Dura: 2 / Nada: 0): '))
            if servico_extra in [0, 1, 2]:
                return servico_extra
            else:
                print('Opção inválida. Por favor, entre com uma opção válida.')
        except ValueError:
            print('Valor inválido. Por favor, entre com um valor numérico.')

#fora de função:
print('Bem-vindo à Copiadora da Bárbara')
print('DIG - Digitalização')
print('ICO - Impressão Colorida')
print('IPB - Impressão Preto e Branco')
print('FOT - Fotocópia')

#obtendo as escolhas do usuário
servico = escolha_servico()
num_pag = num_paginas()
extra = servico_extra()

#valor total a pagar
if servico == 'DIG':
    valor_servico = 1.10
elif servico == 'ICO':
    valor_servico = 1.00
elif servico == 'IPB':
    valor_servico = 0.40
else: #FOT
    valor_servico = 0.20

total = (valor_servico * num_pag)
if extra == 1:
    total += 15
elif extra == 2:
    total += 40

print(f'O total a pagar é de R$ {total:.2f}')