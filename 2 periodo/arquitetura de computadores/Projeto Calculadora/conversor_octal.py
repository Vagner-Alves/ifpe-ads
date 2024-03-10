def decimal(num):
    "Octal para Decimal"
    dec = 0
    potencia = 0

    for digito in num[::-1]:

        dec += int(digito) * (8 ** potencia)

        potencia += 1
    return dec

def binario(num):
    "Octal para Binário"
    binar = ''

    for digito in num:

        binar += format(int(digito) , '03b')
    return binar

def hexadecimal(num):
    "octal para hexadecimal"

    binario = ''
    
    for digito in num:
        binario += format(int(digito), '03b')

    binario = '0' * (4 - len(binario) % 4) + binario

    hex_mapear = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5',
                          '0110': '6', '0111': '7', '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
                          '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}

    hexadecimal = ''
    for i in range(0, len(binario), 4):
        pedaco = binario[i:i+4]
        hexadecimal += hex_mapear[pedaco]

    return hexadecimal


