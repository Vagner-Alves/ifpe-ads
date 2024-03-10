def primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

numeros = []
for i in range(2):
    numeros.append(int(input("Informe um número: ")))

pares = 0
primos = 0


for num in numeros:

    if num % 2 == 0:
        pares += num
    
    if primo(num):
        primos += num

print("Soma dos números Pares:", pares)
print("Soma dos números Primos:", primos)