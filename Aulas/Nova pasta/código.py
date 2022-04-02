# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 11:22:41 2022

@author: halin
"""

import re
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

#Mostrar de um arquivo:
def mostrarImagemDoArquivo (a):
    with open('a.pmg') as f:
        s = f.read()
        l=re.findall(r'[0-9P]+',s)
        w, h = int(l[1]), int(l[2])
        ni = np.array(l[4:],dtype=np.uint8).reshape((h,w))
        from matplotlib import pyplot as plt
        plt.imshow(ni, cmap='gray')
        plt.show()

def mostrarImagem(mapa, save = False, path = "", animation = False, index = 0, direction = ""):
     ni = np.array(mapa)
     plt.imshow(ni, cmap='gray')
     if save == False:
         plt.show()
     if save == True and animation == False:
         plt.savefig(pathToSave.format("output.png"))
     if save == True and animation == True:
         plt.savefig(pathToSave.format(str(index) + "Fig" + direction + ".png"))

mp = [0,0,0,0,0,0,0,0,0,0,0,0]
mapa = []
# adiciona varias vezes o vetor criado a matriz
mapa.append(mp)
mapa.append(mp)
mapa.append(mp)
mapa.append(mp)
mapa.append(mp)
mapa.append(mp)
mapa.append(mp)

# mostra a imagem
mostrarImagem(mapa)

mp = [10,10,10,10,10,10,10,10,10,10,10,10]
mp2 = [0,0,0,0,0,0,0,0,0,0,0,0]
mp3 = [5,5,5,5,5,5,5,5,5,5,5,5]

mapa = []
mapa.append(mp)
mapa.append(mp2)
mapa.append(mp3)
mapa.append(mp2)
mapa.append(mp)
mapa.append(mp3)
mapa.append(mp2)

mostrarImagem(mapa)


def criarImagem(altura, largura, pontosDeCinza):
    vetLargura = []
    for x in range(largura):
        vetLargura.append(0)
    img = []
    for y in range(altura):
        img.append(vetLargura)
    return img

## testa criando uma imagem 50x50
imagem = criarImagem(20,20,15)
mostrarImagem(imagem)

import numpy as np
def escrevePonto(imagem,x,y,pontosDeCinza):
     img = np.array(imagem)
     img[y,x] = pontosDeCinza
     return img
imagem = escrevePonto(imagem,6,5,15)
mostrarImagem(imagem)

###coletando os dados da matriz, para gerar a figura:
M = Image.open('a.jpg')
M = np.asanyarray(M, dtype= np.float32)
print(M)
#transformando a matriz em imagem:
image = Image.fromarray(M)
image.show()

M = Image.open('b.jpg')
M = np.asanyarray(M, dtype= np.float32)
print(M)

image = Image.fromarray(M)
image.show()

M = Image.open('c.jpg')
M = np.asanyarray(M, dtype= np.float32)
print(M)

image = Image.fromarray(M)
image.show()

M = Image.open('d.jpg')
M = np.asanyarray(M, dtype= np.float32)
print(M)

image = Image.fromarray(M)
image.show()

M = Image.open('e.jpg')
M = np.asanyarray(M, dtype= np.float32)
print(M)

image = Image.fromarray(M)
image.show()





    
    

    