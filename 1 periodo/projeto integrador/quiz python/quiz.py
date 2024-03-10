import random
from string import ascii_lowercase
import dados

NUM_QUESTOES = 10


PERGUNTAS = dados.PERGUNTAS

def preparar_questoes(questoes, num_questoes):
    num_questoes = min(num_questoes,len(questoes))
    return random.sample(list(questoes.items()), k=num_questoes)


def pegar_questoes(questao, alternativas):
    print(f"{questao}?")

    indice_de_alternativas = dict(zip(ascii_lowercase, alternativas))

    for indice, alternativa in indice_de_alternativas.items():
        print(f"    {indice}) {alternativa}")
    
    while(indice_resposta :=input('\n Escolha:')) not in indice_de_alternativas:
        print(f"Por favor escolha uma das alternativas: {','.join(indice_de_alternativas)}")
    
    return indice_de_alternativas[indice_resposta]

def fazer_pergunta(questao, alternativas):
    resposta_correta = alternativas[0]

    alternativas_ordenadas = random.sample(alternativas, k=len(alternativas))

    resposta = pegar_questoes(questao, alternativas_ordenadas)
    if resposta == resposta_correta:
        print("⭐ Acertou! ⭐")
        return 1
    else:
        print(f"A resposta é {resposta_correta!r}, não {resposta!r}")
        return 0

def executar_quiz():
    questoes = preparar_questoes(PERGUNTAS, num_questoes=NUM_QUESTOES)

    numero_corretas = 0

    for numero, (questao, alternativas) in enumerate(questoes, start=1):
        print(f"\nPergunta {numero}:")
        numero_corretas += fazer_pergunta(questao, alternativas)

    print(f"\n voce acertou {numero_corretas * 100 / numero}% do Total de Perguntas")
    if numero_corretas >= 8:
        print("Parabéns, seu desempenho foi excelente!")
    elif numero_corretas >= 6 and numero_corretas < 8:
        print("Parabéns, seu desempenho foi bom!")
    else:
        print("Atenção, você precisa estudar mais sobre esse tema")

if __name__ == "__main__":
    executar_quiz()