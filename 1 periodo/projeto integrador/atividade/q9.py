dados = []
while True:
    idades = int(input("\ninforme sua idade"))
    print('digite 0 para sair')

    if idades == 0:
        break
    else:
        dados.append(idades)

print(f"A média das idades registradas é de {sum(dados) / len(dados)}")