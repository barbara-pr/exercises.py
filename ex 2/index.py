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
    preco_item = 0

    if sabor_desejado == 'CP':
        if tamanho == 'P':
            preco_item += 9
        elif tamanho == 'M':
            preco_item += 14
        elif tamanho == 'G':
            preco_item += 18
        total_pedido += preco_item
        print(f'Você pediu um Cupuaçu no tamanho {tamanho}: R${preco_item:.2f}')

    elif sabor_desejado == 'AC':
        if tamanho == 'P':
            preco_item += 11
        elif tamanho == 'M':
            preco_item += 16
        elif tamanho == 'G':
            preco_item += 20
        total_pedido += preco_item
        print(f'Você pediu um Açaí no tamanho {tamanho}: R${preco_item:.2f}')

    continuar_pedido = input('Deseja pedir mais alguma coisa? (s/n): ').lower()
    if continuar_pedido != 's':
        break

print(f'O preço total do seu pedido é R${total_pedido:.2f}')