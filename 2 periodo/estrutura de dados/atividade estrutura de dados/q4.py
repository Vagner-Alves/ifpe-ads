def ler_valores():
    tempo = float(input("Informe o tempo gasto na viagem (em horas): "))
    velocidade_media = float(input("Informe a velocidade média durante a viagem (em km/h): "))
    return tempo, velocidade_media

def calcular_distancia(tempo, velocidade_media):
    distancia = tempo * velocidade_media
    return distancia

def calcular_litros(distancia):
    litros_usados = distancia / 12
    return litros_usados

def apresentar_resultado(tempo, velocidade_media, distancia, litros_usados):
    print(f"Tempo gasto: {tempo:.2f} horas")
    print(f"Velocidade média: {velocidade_media:.2f} km/h")
    print(f"Distância percorrida: {distancia:.2f} km")
    print(f"Litros utilizados: {litros_usados:.2f} litros")

# Programa principal
tempo, velocidade_media = ler_valores()
distancia = calcular_distancia(tempo, velocidade_media)
litros_usados = calcular_litros(distancia)
apresentar_resultado(tempo, velocidade_media, distancia, litros_usados)
