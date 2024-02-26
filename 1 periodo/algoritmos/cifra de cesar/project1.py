# lendo um documento contento a mensagem
with open('/content/arquivo.txt', 'r') as arquivo:
    mensagem = arquivo.read().replace('\n', ', ')

# logica da cifra de cesar

alphabeto = 'abcdefghijklmnopqrstuvwxyz'

def cifrar(texto, rot = 13):
    ''' encriptada: string que retorna a mensagem encriptada ( cifra de cesar)
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
    with open('/content/cifra.txt','w') as arquivo:
        arquivo.write(encriptada)
        
    arquivo.close()
    return encriptada

def descifrar(texto):
    ''' essa função vai descriptografar qualquer mensagem que utilize o padrão cifra de cesar
    utilizado força bruta pra achar a chave de rotação das letras, ou seja, irá retornas todos os 
    resultados possíveis'''

    with open(texto,'r') as arquivo:
        cifra = arquivo.read().replace('\n',',')

    resultado =  open('/content/descifrar.txt','w')
        
        
    for chave in range(26): 
        descriptografia = ''

        for caractere in cifra: 

            if caractere in alphabeto: 


                num = alphabeto.find(caractere)
                num = num - chave
                if num < 0:
                    num = num + 26
                descriptografia += alphabeto[num]
                
               
            else:
                descriptografia += caractere
            
                
                
        print('Descriptografando por Força Bruta\n')
        print(f'chave {chave}: {descriptografia}\n ' )
        
        resultado.write(f'{descriptografia}\n')

    arquivo.close()
    resultado.close()
        
arquivo.close()
