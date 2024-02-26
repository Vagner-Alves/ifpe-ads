import cv2
import numpy as np
import random

def esconder():
  # usa o laço de repetição para encontrar as imagens dentro da pasta 1 e 2
  for x in range(2):
    img1 = cv2.imread(f'/Inserir caminho da primeira pasta / foto{x+1}.jpg')
    img2 = cv2.imread(f'/inserir caminho da segunda pasta /foto{x+1}.jpg')

   # um laço de repetição pra largura, outro para altura e o último variação de 0 a 2  
    for l in range(img2.shape[0]): 
        for a in range(img2.shape[1]): 
          for c in range(3): 
            # v1 e v2 usam o método format para criar uma representação binária de 8 bits para cada imagem
            v1 = format(img1[l][a][c], '08b') 
            v2 = format(img2[l][a][c], '08b') 

            # v3 é a soma entre as duas representações, criando a terceira imagem
            v3 = v1[:4] + v2[:4]  
             # escondendo a imagem dentro da primeira
            img1[l][a][c]= int(v3, 2) 

  # guardando a imagem em outra pasta
    cv2.imwrite(f'inserir caminho da terceira pasta/pic{x+1}.png', img1) 

esconder()


def desfazer():
  for f in range(2):
    img = cv2.imread(f'/Inserir caminho da terceira pasta/pic{f+1}.png')

    width = img.shape[0]
    height = img.shape[1]

    img1 = np.zeros((width, height, 3), np.uint8) 
    img2 = np.zeros((width, height, 3), np.uint8)

    for l in range(width): 
        for a in range(height): 
            for c in range(3): 
                v1 = format(img[l][a][c], '08b') 
                v2 = v1[:4] + chr(random.randint(0, 1)+48) * 4
                v3 = v1[4:] + chr(random.randint(0, 1)+48) * 4
                img1[l][a][c]= int(v2, 2) 
                img2[l][a][c]= int(v3, 2) 

    cv2.imwrite(f'/Inserir caminho da última pasta/result{f+1}.png', img1) 
    cv2.imwrite(f'/Inserir caminho da última pasta /result{f+1}.png', img2)   
