
def x(a):
  if a <= 0:
    return 0
  else:
    return a + x(a-1)

# a função acima faz o calculo de fatorial

# versão iterativa da mesma função

a = 6
print(a + (a -1))
