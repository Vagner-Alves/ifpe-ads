dados = []
while True:
    regiao = input('informe a região:   ')
    idade = int(input('informe sua idade:  '))
    if idade < 0:
        break
    salario = float(input('informe seu salário: '))

    dados.append({'regiao':regiao, 'idade':idade, 'salario':salario})


# calcular a média de salário em cada região
salario_regiao = {}

for habitante in dados:
    if habitante['regiao'] not in salario_regiao:
        salario_regiao[habitante['regiao']] = [habitante['salario']]
    else:
        salario_regiao[habitante['regiao']].append(habitante['salario'])

for regiao, salarios in salario_regiao.items():
    print(f'A média de salário na região de {regiao} é de R${sum(salarios) / len(salarios)}')

# encontrar a maior e menor idade para cada região

idade_regiao = {}

for habitante in dados:
    if habitante['regiao'] not in idade_regiao:
        idade_regiao[habitante['regiao']] = [habitante['idade']]
    else:
        idade_regiao[habitante['regiao']].append(habitante['idade'])

for regiao, idade in idade_regiao.items():
    print(f'A maior idade para a região de {regiao}: {max(idade)} anos')
    print(f'A menorr idade para a região de {regiao}: {min(idade)} anos')

count = 0
for habitante in dados:
    if habitante["idade"] <= 25 and habitante["salario"] > 200:
        count += 1
print(f"\nO número de pessoas com 25 anos e salario acima de R$ 200: {count} pessoas")

# idade e região do maior salário

salario_maior = {}

for habitante in dados:
    if habitante['salario'] > salario_maior:
        salario_maior["salario"] = habitante["salario"]
        salario_maior["idade"] = habitante["idade"]
        salario_maior["regiao"] = habitante["regiao"]
print(f"Idade e região do Maior salário: {salario_maior['idade']} e {salario_maior['regiao']}")

print('fim do programa')
