import conversor_decimal
import conversor_binario
import conversor_octal
import conversor_hexadecimal

while True:

    print('--' * 40)
    print('''Escolha uma base de conversão:

    [1] DECIMAL - converte inteiros em binário, octal e hexadecimal.

    [2] BINARIO - converte binários para decimal, octal e hexadecimal.

    [3] OCTAL - converte octais para decimal, binário e hexadecimal.

    [4] HEXADECIMA - converte hexadecimais para decimal, binário e octal
    
    ''')

    print('--'*40)

    opcao = int(input(" / "))

    if opcao == 1:

        print(''' converter Decimal para 

        [1] BINÁRIO

        [2] OCTAL

        [3] HEXADECIMAL

        [0] SAIR

        ''')

        selecao = int(input("/"))

        numero = float(input("Digite um Número inteiro:"))
        print(f'\n{numero} convertido em Binário é {conversor_decimal.binario(numero)}')

    elif selecao == 2:
        numero = float(input("Digite um Número inteiro:"))
        print(f'\n{numero} convertido em OCtal é {conversor_decimal.octal(numero)}')
       
    
    elif selecao == 3:
        numero = int(input('Digite um Número inteiro: '))
        print(f'\n{numero} convertido em Hexadecimal é {conversor_decimal.hexadecimal(numero)}')

    elif opcao == 2:

        print(''' converter Binário para 

        [1] DECIMAL

        [2] OCTAL

        [3] HEXADECIMAL

        [0] SAIR

        ''')

        selecao = int(input("/"))

        if selecao == 1:
            numero = input("Digite um Número Binário:")
            print(f'\n{numero} convertido em Binário é {conversor_binario.decimal(numero)}')

        elif selecao == 2:
            numero = input("Digite um Número Binário:")
            print(f'\n{numero} convertido em OCtal é {conversor_binario.octal(numero)}')
       
    
        elif selecao == 3:
            numero = input('Digite um Número Binário: ')
            print(f'\n INTEIRO {numero} convertido em Hexadecimal é {conversor_binario.hexadecimal(numero)}')


    elif opcao == 3:

        print(''' converter octal para 

        [1] DECIMAL

        [2] BINARIO

        [3] HEXADECIMAL

        [0] SAIR

        ''')

        selecao = int(input("/"))

        if selecao == 1:
            numero = input("Digite um Número Binário:")
            print(f'\n OCTAL {numero} em DECIMAL : {conversor_octal.decimal(numero)}')

        elif selecao == 2:
            numero = input("Digite um Número Octal:")
            print(f'\n OCTAL {numero}  em BINÁRIO : {conversor_octal.binario(numero)}')
       
    
        elif selecao == 3:
            numero = input('Digite um Número Octal: ')
            print(f'\n OCTAL {numero} em HEXADECIMAL : {conversor_octal.hexadecimal(numero)}')
    
    elif opcao == 4:

        print(''' converter Hexadecimal para 

        [1] DECIMAL

        [2] BINARIO

        [3] OCTAL

        [0] SAIR

        ''')

        selecao = int(input("/"))

        if selecao == 1:
            numero = input("Digite um Número Hexadecimal:")
            print(f'\n HEXADECIMAL  {numero}  em DECIMAL : {conversor_hexadecimal.decimal(numero)}')

        elif selecao == 2:
            numero = input("Digite um Número Hexadecimal:")
            print(f'\n HEXADECIMAL {numero} em BINÁRIO : {conversor_hexadecimal.binario(numero)}')
       
    
        elif selecao == 3:
            numero = input('Digite um Número Hexadecimal: ')
            print(f'\n HEXADECIMAL {numero} em OCTAL : {conversor_hexadecimal.octal(numero)}')
    else:
        break