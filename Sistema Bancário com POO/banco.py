class Usuario:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.conta = None


class ContaCorrente:
    def __init__(self):
        self.saldo = 0
        self.extrato = ''

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f'Depósito: R${valor:.2f}\n'
            print('Depósito realizado com sucesso!')
        else:
            print('Valor de depósito inválido!')

    def sacar(self, valor, limite_valor, limite_saques, saque_quantidade):
        if saque_quantidade < limite_saques:
            if valor <= 0:
                print('Valor de saque inválido!')
            elif self.saldo == 0:
                print('Não será possível sacar o dinheiro por falta de saldo!')
            elif valor > limite_valor:
                print('Limite de valor por saque ultrapassado!')
            elif valor > self.saldo:
                print('Saldo insuficiente!')
            else:
                self.saldo -= valor
                saque_quantidade += 1
                self.extrato += f'Saque: R${valor:.2f}\n'
                print('Saque realizado com sucesso!')
                return saque_quantidade
        else:
            print('Limite de saques diários atingido!')
        return saque_quantidade

    def mostrar_extrato(self):
        print('-' * 20)
        print('\nExtrato:')
        print(self.extrato if self.extrato else 'Não foram realizadas movimentações.')
        print(f'Saldo atual: R${self.saldo:.2f}\n')
        print('-' * 20)


class Banco:
    def __init__(self):
        self.usuarios = {}

    def criar_usuario(self, nome, cpf):
        if cpf in self.usuarios:
            print('Usuário já cadastrado.')
        else:
            self.usuarios[cpf] = Usuario(nome, cpf)
            print(f'Usuário {nome} criado com sucesso!')

    def criar_conta_corrente(self, cpf):
        if cpf not in self.usuarios:
            print('Usuário não encontrado. Crie um usuário primeiro.')
        elif self.usuarios[cpf].conta is not None:
            print('Conta já existente para este usuário.')
        else:
            self.usuarios[cpf].conta = ContaCorrente()
            print('Conta corrente criada com sucesso!')


def main():
    banco = Banco()
    saque_quantidade = 0
    LIMITE_VALOR = 500
    LIMITE_SAQUES = 3

    menu = '''
    [c] Criar Usuário
    [cc] Criar Conta Corrente
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [x] Sair
    '''

    while True:
        opcao = input(menu).lower()

        if opcao == 'c':
            nome = input('Digite o nome do usuário: ')
            cpf = input('Digite o CPF do usuário: ')
            banco.criar_usuario(nome, cpf)

        elif opcao == 'cc':
            cpf = input('Digite o CPF do usuário para criar a conta: ')
            banco.criar_conta_corrente(cpf)

        elif opcao == 'd':
            cpf = input('Digite o CPF do usuário: ')
            if cpf in banco.usuarios and banco.usuarios[cpf].conta:
                valor = float(input('Digite o valor do depósito: '))
                banco.usuarios[cpf].conta.depositar(valor)
            else:
                print('Usuário ou conta não encontrados.')

        elif opcao == 's':
            cpf = input('Digite o CPF do usuário: ')
            if cpf in banco.usuarios and banco.usuarios[cpf].conta:
                valor = float(input('Digite o valor do saque: '))
                saque_quantidade = banco.usuarios[cpf].conta.sacar(valor, LIMITE_VALOR, LIMITE_SAQUES, saque_quantidade)
            else:
                print('Usuário ou conta não encontrados.')

        elif opcao == 'e':
            cpf = input('Digite o CPF do usuário: ')
            if cpf in banco.usuarios and banco.usuarios[cpf].conta:
                banco.usuarios[cpf].conta.mostrar_extrato()
            else:
                print('Usuário ou conta não encontrados.')

        elif opcao == 'x':
            print('Finalizando o programa...')
            break

        else:
            print('Opção inválida. Tente novamente.')


if __name__ == "__main__":
    main()
