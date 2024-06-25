print('Sabendo que a=5,122132 x 10^3 e que b=2,741826 x 10^3, calcule a+b por meio do Python.')
a = 5.122132e+03
b = 2.741826e+03
c = a + b
print('%.10e' % c)

print('-' * 15)

print('Por meio do Python, calcule a.b onde a=3,445161 x 10^3 e b=1,151436 x 10^3.')
a = 3.445161e+03
b = 1.151436e+03
c = a * b
print('%.12e' % c)

print('-' * 15)

print('Por meio do Python, faça a representação do número 0,0126551 utilizando a notação científica normalizada com 6 casas decimais.')
print('%.6e' % 0.0126551)

print('-' * 15)

print('Dados os números decimais a=1,758911 x 10^2 e b=4,002234 x 10^5, por meio do Python, calcule a+b.')
a = 0.001758911e+05
b = 4.002234e+05
c = a + b
print('%.10e' % c)

print('-' * 15)

print('Considerando os números decimais a=3,445161 x 10^3 e b=1,151436 x 10^3,calcule a/b por meio do Python.')
a = 3.445161e+03
b = 1.151436e+03
c = a/b
print('%.10e' % c)

print('-' * 15)

print('A área de um círculo é dada pela expressão 𝐴 = π𝑟 . Calcule a área referente a 2 um círculo de raio 12 cm considerando π = 3, 14 e considerando em seguida π = 3, 14159265. Calcule, por meio do Python, o erro absoluto e o erro relativo entre os dois resultados obtidos.')
A1 = 3.14 * 12**2
A2 = 3.14159265 * 12**2
erroAbsoluto = abs(A2 - A1)
erroRelativo = abs(A2 - A1) / abs(A2)
erroRelativoPorcentagem = (abs(A2 - A1) / abs(A2)) / 0.01

print(f'O erro absoluto foi de: {erroAbsoluto:.9f}')
print(f'O erro relativo foi de: {erroRelativo:.9f} ou {erroRelativoPorcentagem:.9f}%')