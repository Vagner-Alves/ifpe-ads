# defina uma funçaõ recursiva em python que recebe como argumento uma lista de listas de números inteiros
# w e devolve o número de elementos pares que existem nas sublistas
def par(lista):
    if lista == []:
        return 0
    
    elif lista[0]%2==0:
        return 1 + par(lista[1:])
    else:
        return par(lista[1:])

def g1(w):
    if w == []:
        return 0
    else:
        return par(w[0]) + g1(w[1:])

lista = [[1,4,3,1],[3,5,7],[],[8,0,6]]
print(g1(lista))


# defina uma função recursiva g2 que recebe como argumento uma lista de listas de números inteiros w e devolve True se em todas as sublistas de w existir um número positivo.

def positivo(lista):
    if lista == []:
        return False
    elif lista[0]>0:
        return True or positivo(lista[1::])
    else:
        return False or positivo(lista[1:])

def g2(w):
    if w == []:
        return True
    else:
        return positivo(w[0]) and g2(w[1::])

lista2 = [[1,4,3,1],[3,5,7],[],[8,0,6]]
print(g2(lista2))

# defina uma função recursiva g3 que recebe como argumento uma lista de listas de números inteiros
#e devolve True se alguma das listas em w tiver mais pares do que ímpares e False caso contrário.
# a função se utiliza da outra função par() definida acima.

def g3(w):
    if w == []:
        return False
    else:
        if len(w[0])/2 > par(w[0]):
            return True 
        else:
            return False or g3(w[1:])

print(g3(lista2))

''' defina uma função recursiva g4 que como argumento uma lista de listas de números inteiros w e devolve True
se todas as listas em w tiverem mais da metade dos seus elementos igual a 0 e False caso contrário, definir também funções auxiliares desde que sejam recursivas
'''

def quant(lista):
    if lista == []:
        return 0
    elif lista[0] == 0:
        return 1 + quant(lista[1:])
    else:
        return quant(lista[1:])
 
def g4(w):
    if w == []:
        return 0
    else:
        tamanho = len(w[0]) /2
        if tamanho < quant(w[0]):
            return True 
        else:
            return False and g4(w[1:])

lista3 = [[0,0,3,0],[0,5,0],[0,0,0]]

print(g4(lista2))

'''defina uma função recursiva g5 que recebe como argumento uma lista de listas de números inteiros,
e devolve True se cada lista em w tiver o mesmo número de elementos positivos e negativos,
e False caso contrário.'''

def positivo(lista):
    if lista == []:
        return 0
    elif lista[0] > 0:
        return 1 + positivo(lista[1:])
    else:
        return positivo(lista[1:])

def negativo(lista):
    if lista == []:
        return 0
    elif lista[0] < 0:
        return 1 + negativo(lista[1:])
    else:
        return negativo(lista[1:])

def g5(w):
    if w == []:
        return False
    elif positivo(w[0]) == negativo(w[0]):
        return True
    else:
        return False and g5(w[1:])

lista4 = [[2,4,-3,-1],[-3,0,7],[-8,6]]

print(g5(lista4))