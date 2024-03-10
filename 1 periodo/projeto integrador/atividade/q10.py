
while True:
    print(''' Escolha uma opção
    1-Média aritmética
    2-Média Ponderada
    3-Sair

''')

    
    opcao = int(input("\n digite..."))

    if opcao not in [1,2,3]:
        print('Opção invalída, por favor escolha novamente.')
    
    elif opcao == 3:
        break

    elif opcao == 1:
        num1 = int(input("digite uma nota"))
        num2 = int(input("digite uma segunda nota"))

        media = num1 + num2 / 2
        print('a média aritmética é de ', media)
    elif opcao == 2:
        nota1 = int(input('informe a primeira nota: '))
        peso1 = int(input('\ninforme o peso da primeira nota: '))
        nota2 = int(input('informe a segunda nota:  '))
        peso2 = int(input('\ninforme o peso da segunda nota:  '))
        nota3 = int(input('informe a terceira nota:  '))
        peso3 = int(input('\ninforme o peso da Terceira nota:  '))

        media = (nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)
        media2 =  peso1 + peso2 + peso3 

        print('A média Ponderada é ', media / media2)
