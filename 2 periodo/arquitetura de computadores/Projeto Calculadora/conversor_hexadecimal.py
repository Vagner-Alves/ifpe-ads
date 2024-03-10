def decimal(num):
    "Hexadecimal para Decimal"

    dec = 0
    potencia = 0

    for digito in num[::-1]:

        dec += int(digito , 16) * (16 ** potencia)

        potencia += 1
    return dec


def binario(num):
    "Converte hexadecimal para binario"
    binari = ''

    for digito in num:
        binari += format(int(digito, 16),'04b')

    return binari

def octal(hexadecimal):
    """Converte hexadecimal para octal."""
    binar = ''
   
    for digit in hexadecimal:
       
        binar += format(int(digit, 16), '04b')

   
    binar = '0' * (3 - len(binar) % 3) + binar

    octal = ''
    
    for i in range(0, len(binar), 3):
        chunk = binar[i:i+3]
       
        octal += str(int(chunk, 2))

    return octal