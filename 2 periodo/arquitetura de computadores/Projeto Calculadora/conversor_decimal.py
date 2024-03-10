def binario(num):
    "converte decimal para binário"
    binari = ''
    x = 0

    while num > 0 and x <=8:
        text = str(int(num%2))
        binari = binari + text

        num /= 2
        x = x + 1
        resultado = binari[::-1]

    return resultado

def octal(num):
    "converter decimal para octal"
    octal = 0
    contador = 1

    while num > 0:

        x = num % 8

        octal += x * contador

        contador *= 10

        num = num // 8

    return octal

def hexadecimal(num):
    "converter decimal para hexadecimal"
    hexa = []

    while num != 0:

        x = num % 16

        if x < 10:
            hexa.append(chr( x + 48))

        else:
            hexa.append(chr(x + 55))

        num = num // 16
    
    hexa.reverse()

    return ''.join(hexa)

