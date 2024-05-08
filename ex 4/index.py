print('Bem-vindo à Livraria da Bárbara')

lista_livro = []
id_global = 0

#cadastrar livro
def cadastrar_livro(id):
    global id_global
    nome = input('Entre com o nome do livro: ')
    autor = input('Entre com o nome do autor: ')
    editora = input('Entre com o nome da editora: ')
    livro = {'id': id, 'nome': nome, 'autor': autor, 'editora': editora}
    lista_livro.append(livro)
    id_global += 1

#consultar todos os livros
def consultar_todos():
    print('--- Lista de Livros ---')
    for livro in lista_livro:
        print(f'ID: {livro["id"]}, Nome: {livro["nome"]}, Autor: {livro["autor"]}, Editora: {livro["editora"]}')
    print('-----------------------')

#consultar livro por ID
def consultar_por_id():
    id_consulta = int(input('Entre com o ID do livro: '))
    for livro in lista_livro:
        if livro['id'] == id_consulta:
            print(f'Nome: {livro["nome"]}, Autor: {livro["autor"]}, Editora: {livro["editora"]}')
            return
    print('Livro não encontrado.')

#consultar livro por autor
def consultar_por_autor():
    autor_consulta = input('Entre com o nome do autor: ')
    encontrados = False
    for livro in lista_livro:
        if livro['autor'] == autor_consulta:
            print(f'ID: {livro["id"]}, Nome: {livro["nome"]}, Editora: {livro["editora"]}')
            encontrados = True
    if not encontrados:
        print('Nenhum livro encontrado desse autor.')

#remover livro por ID
def remover_livro():
    id_remover = int(input('Entre com o ID do livro a ser removido: '))
    for livro in lista_livro:
        if livro['id'] == id_remover:
            lista_livro.remove(livro)
            print('Livro removido com sucesso.')
            return
    print('ID inválido. Livro não encontrado.')

while True:
    print('--------------------------------')
    print('-------- MENU PRINCIPAL --------')
    print('1 - Cadastrar Livro')
    print('2 - Consultar Livro (s)')
    print('3 - Remover Livro')
    print('4 - Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        cadastrar_livro(id_global)
    elif opcao == '2':
        while True:
            print('--- Consultar Livro ---')
            print('1 - Consultar Todos')
            print('2 - Consultar por ID')
            print('3 - Consultar por Autor')
            print('4 - Retornar ao menu')

            opcao_consulta = input('Escolha uma opção: ')
            if opcao_consulta == '1':
                consultar_todos()
            elif opcao_consulta == '2':
                consultar_por_id()
            elif opcao_consulta == '3':
                consultar_por_autor()
            elif opcao_consulta == '4':
                break
            else:
                print('Opção inválida.')
    elif opcao == '3':
        remover_livro()
    elif opcao == '4':
        break
    else:
        print('Opção inválida.')
