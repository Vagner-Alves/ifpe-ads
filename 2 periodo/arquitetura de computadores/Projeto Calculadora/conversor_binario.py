def decimal(num):
    "converte binário para decimal"
    dec = 0
    i = 0

    while (num != 0):
        x = num % 10

        dec =  dec + x * pow(2, i)

        num =  num // 10

        i += 1
    return dec

def octal(num):
    "converte binário para octal"

    while len(num) % 3 != 0:
        num = 'O' + num
    
    mapear_octal = {'000': '0', '001': '1', '010': '2', '011': '3', '100': '4', '101': '5', '110': '6', '111': '7'}

    oct = ''

    for i in range(0, len(num), 3):
        pedaco = num[i:i + 3]
        oct += mapear_octal[pedaco]
    return oct

def hexadecimal(num):
    "Converte Binário para Hexadecimal"

    num = '0' * (4 - len(num) % 4) + num

    mapear_hexa = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5',
                          '0110': '6', '0111': '7', '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
                          '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}
    
    hexadecim = ''
    # Iterate through the binary number in chunks of 4 digits
    for i in range(0, len(num), 4):
        chunk = num[i:i+4]
        hexadecim += mapear_hexa[chunk]
    return hexadecim




