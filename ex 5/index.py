#como essa rotina não nos retorna nada, chamamos de procedimento
def borda (s1):
    tam = len(s1)
    #só vai executar se tiver algum caractere
    if tam:
        print('+', '-' * tam, '+')
        print('|', s1, '|')
        print('+', '-' * tam, '+')

#chamando a função e passando os parâmetros
borda('Olá, Mundo!')
borda('Lógica de Programação e Algoritmos.')
borda('Bárbara')