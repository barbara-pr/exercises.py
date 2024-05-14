# Escreva um algoritmo que crie uma tupla com 5 palavras. Encontre dentro dessa tupla as vogais de cada palavra. Faça
# um print na tela com o nome da respectiva palavra e suas respectivas vogais.

frutas = ('Abacaxi', 'Uva', 'Maçã', 'Tangerina', 'Melancia')

for fruta in frutas:
    print(f'\n Frutas {fruta.upper()}. Vogais: ')
    for letra in fruta:
        if letra.lower() in 'aeiou':  # se a letra (minúscula) estiver contida em 'aeiou'
            print(letra.upper(), end=' ')