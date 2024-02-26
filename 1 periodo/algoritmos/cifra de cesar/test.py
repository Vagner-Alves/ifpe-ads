# lendo um documento contento a mensagem
with open('arquivo.txt', 'r') as arquivo:
    mensagem = arquivo.read().replace('\n', ', ')

# logica da cifra de cesar

alphabeto = 'abcdefghijklmnopqrstuvwxyz'


def cifrar(texto,rot = 13):
    ''' encriptada: string que retorna a mensagem encripatada ( cifra de cesar)
        indice: posição de cada letra na string
        dentro do laço FOR encontramos a posição ( indice) de cada letra e usamos a rotação (ROT) para
        encriptar de acordo com a cifra de cesar
        a condicional ( if else) ajuda a resolver problemas com espacos entre as palavras as adicionando normalmente na string
        e por fim os dados são escritos em um arquivo.txt 
        '''
    encriptada = ''
    for letra in texto:
        if letra in alphabeto:
            indice = alphabeto.index(letra)
            encriptada += alphabeto[(indice + rot) % len(alphabeto)]
        else:
            encriptada += letra
    with open('cifra.txt','w') as arquivo:
        arquivo.write(encriptada)
        
    arquivo.close()
    return encriptada


def descifrar(texto):
    

    with open(texto,'r') as arquivo:
        cifra = arquivo.read().replace('\n',',')

    resultado =  open('descifrar.txt','w')
        
        
    for chave in range(26): 
        descriptografia = ''

        for caractere in cifra: 

            if caractere in alphabeto: 


                num = alphabeto.find(caractere)
                num = num - chave
                if num < 0:
                    num = num + 26
                descriptografia = descriptografia + alphabeto[num]
                
               
            else:
                descriptografia = descriptografia + caractere
            
                
                
        print('Descriptografando por Força Bruta\n')
        print(f'chave {chave}: {descriptografia}\n ' )
        
        resultado.write(f'{descriptografia}\n')

    arquivo.close()
    resultado.close()
        
arquivo.close()

