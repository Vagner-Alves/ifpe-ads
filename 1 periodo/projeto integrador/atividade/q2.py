idades = [ [], [] , [] , [] , [], []

]

for x in range(1,16):
    idade = int(input("\nPor favor digite sua idade: "))
    idades[0].append(idade)
    if idade <= 15:
        idades[1].append(idade)

    elif idade >= 16 and idade <= 30:
        idades[2].append(idade)
    
    elif idade >= 31 and idade <= 45:
        idades[3].append(idade)
    
    elif idade >= 46 and idade <= 60:
        idades[4].append(idade)

    else:
        idades[5].append(idade)
    
      
print(f'\nfaixa etária 1 ( até 15 anos) tem um total de : {len(idades[1])} pessoas')
print(f'\nfaixa etária 2 (De 16 a 30 anos ) tem um total de : {len(idades[2])} pessoas')
print(f'\nfaixa etária 3 ( De 31 a 45 anos) tem um total de : {len(idades[3])} pessoas')
print(f'\nfaixa etária 4 ( De 46 a 60 anos) tem um total de : {len(idades[4])} pessoas')
print(f'\nfaixa etária 5 ( Acima de 60 anos) tem um total de : {len(idades[5])} pessoas')


percen_faixa1 = len(idades[1]) * 100 // len(idades[0])
percen_faixa2 = len(idades[5]) * 100 // len(idades[0])
print(f'\na porcentagem de pessoas na primeira e na última faixa etária, são {percen_faixa1} % e {percen_faixa2}% com relação ao total de {len(idades[0])} pessoas')
