# Sistema Bancário com funcionalidades de saque, depósito e extrato

saque_quantidade = 0
saldo_atual = 0
LIMITE_VALOR = 500
LIMITE_SAQUES = 3
extrato = ''

menu = '''
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [x] Sair
'''

while True:
    opcao = input(menu).lower()

    if opcao == 'd':
        deposito_valor = float(input('Digite o valor do depósito: '))
        if deposito_valor > 0:
            saldo_atual += deposito_valor
            extrato += f'Depósito: R${deposito_valor:.2f}\n'
        else:
            print('Valor de depósito inválido!')

    elif opcao == 's':
        if saque_quantidade < LIMITE_SAQUES:
            saque_valor = float(input('Digite o valor do saque: '))
            if saque_valor <= 0:
                print('Valor de saque inválido!')
            if saldo_atual == 0:
                print('Não será possível sacar o dinheiro por falta de saldo!')
            elif saque_valor > LIMITE_VALOR:
                print('Limite de valor por saque ultrapassado!')
            elif saque_valor > saldo_atual:
                print('Saldo insuficiente!')
            else:
                saldo_atual -= saque_valor
                saque_quantidade += 1
                extrato += f'Saque: R${saque_valor:.2f}\n'
        else:
            print('Limite de saques diários atingido!')

    elif opcao == 'e':
        print('-' * 20)
        print('\nExtrato:')
        print(extrato if extrato else 'Não foram realizadas movimentações.')
        print(f'Saldo atual: R${saldo_atual:.2f}\n')
        print('-' * 20)

    elif opcao == 'x':
        print('Finalizando o programa...')
        break

    else:
        print('Opção inválida. Tente novamente.')
