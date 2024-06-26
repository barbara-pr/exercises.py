import numpy as np

# Matriz
print('Criando uma matriz:')
A = np.array([[3, 2, -1], [5, 0, 20]])
print(A)

print('-' * 15)

print('Somando matrizes')
F1 = np.array([[400, 10], [480, 12], [600, 15]])
F2 = np.array([[31, 11], [37, 11], [48, 11]])
custoTotal = F1 + F2
print(custoTotal)

print('-' * 15)

# Gerar um conjunto de números inteiros que variam de -10 a 20 e verificar se o número -1 está neste conjunto.
conjunto = []
for i in range(-10, 21):
    conjunto.append(i)
print(conjunto)
print(-1 in conjunto)

print('-' * 15)

# Ver se a senha digitada contém na lista de senhas permitidas
senhas = [452012, 323233, 787910, 528917, 683524]
senhaUser = int(input('Digite sua senha: '))
print(senhaUser in senhas)

print('-' * 15)
# Retornar os preços com desconto
v = np.array([[1210, 897, 1230, 1495, 799, 890, 1010]])
d = 0.2 * v
n = v - d
print(f'Os preços com desconto: {n}')

print('-' * 15)
# Somando matrizes
A = np.array([[3, 5, 9], [4, 2, -3], [1, 5, -5]])
B = np.array([[12, -6, 7], [3, 0, 2], [-1, 10, 1]])
soma = A +B
print(soma)

print('-' * 15)
# Multiplicando matrizes
A = np.array([[3, 5, 9], [4, 2, -3], [1, 5, -5]])
B = np.array([[12, -6, 7], [3, 0, 2], [-1, 10, 1]])
multiplicacao = np.matmul(A, B)
print(multiplicacao)
