import random
from string import ascii_lowercase

num_questoes = 4
PERGUNTAS = {
    'Quando foi a primeira vez que a palavra quiz foi usada':['1781',
    '1818','2023',
    '2012','1994'],

    'quanto tempo durou a ditadura da era vargas?':['15 anos',
    '200 anos','8 anos','2 anos','70 anos'],
    
    'qual escola literaria onde a emoção predominava sobre a razão?':['romantismo', 'barroco','realismo','iluminismo', 
    'modernismo'],

    'Quando o individuo modifica seu rosto através de uma cirurgia plástica, determine':['fenótipo','genótipo','genética']
}

num_perguntas = min(num_questoes, len(PERGUNTAS))

perguntas = random.sample(list(PERGUNTAS.items()), k = num_perguntas)

num_corretas = 0

for numero, (perguntas, alternativas) in enumerate(perguntas, start=1):
    print(f"\nPerguntas {numero}:")
    print(f"{perguntas}?")
    resposta_correta = alternativas[0]

    alternativas_indice = dict(zip(ascii_lowercase, random.sample(alternativas, k=len(alternativas))))
    for indice, alternativa in alternativas_indice.items():
        print(f"  {indice}) {alternativa}")

    while( indice_resposta:= input('\n Escolha a questão:   ')) not in alternativas_indice:
        print(f"Por favor, responda uma das alternativas disponíveis: {','.join(alternativas_indice)}")

    resposta = alternativas_indice[indice_resposta]
    if resposta == resposta_correta:
        num_corretas += 1
        print("⭐ Resposta Correta! ⭐")
    else:
        print(f"A resposta é {resposta_correta!r}, não {resposta!r}")

print(f'\n voce acertou {num_corretas} questões de um total de {numero} ')
