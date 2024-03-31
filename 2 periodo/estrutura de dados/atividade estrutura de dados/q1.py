numeros = []
soma = 0

for x in range(1,6):
    num = int(input("digite um número:  "))
    numeros.append(num)

for y in numeros:
    soma += y

print(soma)