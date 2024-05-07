print('Bem-vindo à Loja de Gelados da Bárbara')
print('--------------------Cardápio--------------------')
print('------------------------------------------------')

print('---| Tamanho| Cupuaçu (CP) | Açaí (AC) |---')
print('---|    P   |    R$9,00    |  R$11,00  |---')
print('---|    M   |    R$14,00   |  R$16,00  |---')
print('---|    G   |    R$18,00   |  R$20,00  |---')
print('------------------------------------------------')

total_pedido = 0

# permitir pedidos múltiplos
while True:
    sabor_desejado = input('Entre com o sabor desejado (CP/AC): ').upper()
    tamanho = input('Entre com o tamanho desejado (P/M/G): ').upper()

    if sabor_desejado != 'CP' and sabor_desejado != 'AC' and sabor_desejado != 'cp' and sabor_desejado != 'ac':
        print('Pedido com sabor inválido')
        continue

    if tamanho != 'P' and tamanho != 'M' and tamanho != 'G' and tamanho != 'p' and tamanho != 'm' and tamanho != 'g':
        print('Pedido com tamanho inválido')
        continue

    # atualizando o preço total do pedido com base no sabor e tamanho escolhidos
    if sabor_desejado == 'CP':
        if tamanho == 'P':
            total_pedido += 9
        elif tamanho == 'M':
            total_pedido += 14
        elif tamanho == 'G':
            total_pedido += 18

    elif sabor_desejado == 'AC':
        if tamanho == 'P':
            total_pedido += 11
        elif tamanho == 'M':
            total_pedido += 16
        elif tamanho == 'G':
            total_pedido += 20

    continuar_pedido = input('Deseja pedir mais alguma coisa? (s/n): ').lower()
    if continuar_pedido != 's':
        break

print(f'O preço total do seu pedido é R${total_pedido:.2f}')