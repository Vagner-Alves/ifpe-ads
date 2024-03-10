def tabuada(numero, t = 0):
    x = 10
    if t >= 10:
        return 0
    print(f'{numero} x {t + 1} = {numero*(t + 1)}')
    

    tabuada(numero, t + 1)  

for x in range(1,11):
    tabuada(x)
    print('\n')

