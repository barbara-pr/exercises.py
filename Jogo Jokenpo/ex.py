import random

def validar(pergunta, min, max):
    x = int(input(pergunta))
    while x < min or x > max:
        x = int(input(pergunta))
    return x

def vencedor(jogador1, jogador2):
    global v1, v2, empate
    if jogador1 == 1:  # Pedra
        if jogador2 == 1:  # Pedra
            empate += 1
        elif jogador2 == 2:  # Papel
            v2 += 1
        elif jogador2 == 3:  # Tesoura
            v1 += 1
    elif jogador1 == 2:  # Papel
        if jogador2 == 1:  # Pedra
            v1 += 1
        elif jogador2 == 2:  # Papel
            empate += 1
        elif jogador2 == 3:  # Tesoura
            v2 += 1
    elif jogador1 == 3:  # Tesoura
        if jogador2 == 1:  # Pedra
            v2 += 1
        elif jogador2 == 2:  # Papel
            v1 += 1
        elif jogador2 == 3:  # Tesoura
            empate += 1

    resultados = [v1, v2, empate]
    return resultados

print('JOKENPÔ')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')

jogadas = []
v1 = 0
v2 = 0
empate = 0

while True:
    j1 = validar('Escolha sua jogada (1-Pedra, 2-Papel, 3-Tesoura, 0-Para sair): ', 0, 3)
    if j1 == 0:
        break
    j2 = random.randint(1, 3)
    jogadas.append([j1, j2])
    resultados = vencedor(j1, j2)

print("\nResultados das jogadas:")
for jogada in jogadas:
    j1, j2 = jogada
    jogada_str = ["Pedra", "Papel", "Tesoura"]
    print(f"Jogador: {jogada_str[j1 - 1]}, Computador: {jogada_str[j2 - 1]}")

print(f'\nNúmero de vitórias do jogador 1: {resultados[0]}')
print(f'Número de vitórias do jogador 2: {resultados[1]}')
print(f'Número de empates: {resultados[2]}')
