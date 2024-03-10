dados = []
pes = 0
alt = []
for x in range(1,10+1):
    idade = int(input("informe sua idade:   "))
    altura = float(input("informe sua altura: "))
    peso = int(input("informe seu peso: "))

    dados.append([idade, altura, peso])

    if peso > 90 and altura < 1.50:
        pes +=1
    elif idade >=10 and idade <=30 and altura > 1.90:
        alt.append(altura)

print(f'pessoas com peso acima de 90kg e altura menor que 1.50 {pes}')
print(f'Percentual com mais de 1.90 entre 10 a 30 anos {len(alt) * 100 / len(dados)}% do total')


