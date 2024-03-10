n = int(input("Digite um número (inteiro)"))

soma = 0

for x in range(1,n+1, 2):
    print(x)
    soma += x

print(f'A soma dos ímpares de 1 a {n} é: {soma}')
