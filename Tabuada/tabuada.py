# Ler um número e mostrar a tabuada dele

while True:
    try:
        num = int(input('Digite um número: '))
        break
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

print('-' * 15)

contador = 1
while contador <= 10:
    print(f'{num} x {contador} = {num * contador}')
    contador += 1