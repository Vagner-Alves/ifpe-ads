num = []
while True:

    entrada = int(input("\nInforme números inteiros positivos: "))
    print("\ndigite 0 para sair")

    if entrada == 0:
        print("\nPrograma encerrado")
        break
    elif entrada < 0:
        print(f"Valores negativos ex:{entrada} não são aceitos")
    else:
        num.append(entrada)

print(f"O maior valor do conjunto é {max(num)}")
print(f"O menor valor do conjunto é {min(num)}")