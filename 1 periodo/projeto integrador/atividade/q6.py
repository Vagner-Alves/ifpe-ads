# ler idade, peso e altura de 25 pessoas
# quantidade de pessoas com idade superior a 50 anos
# média de altura das pessoas entre 10 e 20 anos
# percentual de pessoas com peso inferior a 40kg do total

dados = []
alt = []
pes = []
ida = []

for x in range(1,25 + 1):
    idade = int(input("informe sua idade:   "))
    altura = float(input("informe sua altura: "))
    peso = int(input("informe seu peso: "))

    dados.append([idade, altura, peso])
    if idade >= 10 and idade <=20:
        alt.append(altura)

    pes.append(peso)
    ida.append(idade)

for idade in ida:
    cont = 0
    if idade > 50:
        cont +=1
        print(f'O número de pessoas com mais de 50 anos é {cont}')

for peso in pes:
    cont = 0
    if peso < 40:
        cont +=1
        print(f"As pessoas com peso inferior a 40kg é {cont * 100 / len(dados)}% do total")

print(f" a média de altura das pessoas cadastradas é de {sum(alt) / len(alt)}")

