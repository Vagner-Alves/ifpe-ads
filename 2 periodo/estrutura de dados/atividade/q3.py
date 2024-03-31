def ler():
    return float(input('Informar Temperatura em Graus Celsius:  '))

def calculo(temperatura):
    f = (9 * temperatura + 160) / 5
    return f

def resultado(f):
    print(f"A temperatura em fahrenheit é {f:.2f}")

temperatura = ler()

converter = calculo(temperatura)

resultado(converter)
