# Sistema Bancário com funcionalidades de saque, depósito, extrato, criação de usuário e conta corrente

saque_quantidade = 0
saldo_atual = 0
LIMITE_VALOR = 500
LIMITE_SAQUES = 3
extrato = ''
usuarios = {}  # Dicionário para armazenar usuários

menu = '''
    [c] Criar Usuário
    [cc] Criar Conta Corrente
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [x] Sair
'''

def criar_usuario(nome, cpf):
    if cpf in usuarios:
        print('Usuário já cadastrado.')
    else:
        usuarios[cpf] = {'nome': nome, 'conta': None}
        print(f'Usuário {nome} criado com sucesso!')

def criar_conta_corrente(cpf):
    if cpf not in usuarios:
        print('Usuário não encontrado. Crie um usuário primeiro.')
    elif usuarios[cpf]['conta'] is not None:
        print('Conta já existente para este usuário.')
    else:
        usuarios[cpf]['conta'] = {'saldo': 0, 'extrato': ''}
        print('Conta corrente criada com sucesso!')

def depositar(saldo_atual, extrato, /):  # Apenas posicionais
    deposito_valor = float(input('Digite o valor do depósito: '))
    if deposito_valor > 0:
        saldo_atual += deposito_valor
        extrato += f'Depósito: R${deposito_valor:.2f}\n'
        print('Depósito realizado com sucesso!')
    else:
        print('Valor de depósito inválido!')
    return saldo_atual, extrato

def sacar(*, saque_quantidade, saldo_atual, extrato):  # Apenas por nome
    if saque_quantidade < LIMITE_SAQUES:
        saque_valor = float(input('Digite o valor do saque: '))
        if saque_valor <= 0:
            print('Valor de saque inválido!')
        elif saldo_atual == 0:
            print('Não será possível sacar o dinheiro por falta de saldo!')
        elif saque_valor > LIMITE_VALOR:
            print('Limite de valor por saque ultrapassado!')
        elif saque_valor > saldo_atual:
            print('Saldo insuficiente!')
        else:
            saldo_atual -= saque_valor
            saque_quantidade += 1
            extrato += f'Saque: R${saque_valor:.2f}\n'
            print('Saque realizado com sucesso!')
    else:
        print('Limite de saques diários atingido!')
    return saque_quantidade, saldo_atual, extrato

def mostrar_extrato(extrato, saldo_atual, /, *, titulo='Extrato'):  # Posicionais e keyword only
    print('-' * 20)
    print(f'\n{titulo}:')
    print(extrato if extrato else 'Não foram realizadas movimentações.')
    print(f'Saldo atual: R${saldo_atual:.2f}\n')
    print('-' * 20)

while True:
    opcao = input(menu).lower()

    if opcao == 'c':
        nome = input('Digite o nome do usuário: ')
        cpf = input('Digite o CPF do usuário: ')
        criar_usuario(nome, cpf)

    elif opcao == 'cc':
        cpf = input('Digite o CPF do usuário para criar a conta: ')
        criar_conta_corrente(cpf)

    elif opcao == 'd':
        saldo_atual, extrato = depositar(saldo_atual, extrato)

    elif opcao == 's':
        saque_quantidade, saldo_atual, extrato = sacar(saque_quantidade=saque_quantidade, saldo_atual=saldo_atual, extrato=extrato)

    elif opcao == 'e':
        mostrar_extrato(extrato, saldo_atual)

    elif opcao == 'x':
        print('Finalizando o programa...')
        break

    else:
        print('Opção inválida. Tente novamente.')
int()