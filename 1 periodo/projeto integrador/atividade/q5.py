compras = [[],[]

]

def valores():
    for x in range(1,16):
        codigo = int(input("Informe o código da Transação: 0 para compras a vista 1 a prazo;  "))

        valor = int(input('informa e valor da da compra: R$'))

        if codigo == 1:
            compras[1].append(valor)
        else:
            compras[0].append(valor)

valores()

print(f'\nValor total das compras à vista; R${sum(compras[0])}')
print(f'Valor total das transações à prazo; R${sum(compras[1])}')
print(f'valor total das compras efetuadas; R${sum(compras[0]) + sum(compras[1])}')
print(f'o valor da primeira prestação das compras a prazo juntas: R${sum(compras[1])/3:.2f}')