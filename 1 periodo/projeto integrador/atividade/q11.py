dados = []
 
while True:
    idade = int(input('\n informe a sua idade:  '))
    altura = float(input('informe sua altura:   '))

    if idade <= 0:
        break
    elif idade > 50:
        dados.append(altura)

print(f'A média de altura das pessoas com mais de 50 anos é {sum(dados)/len(dados)}metros')