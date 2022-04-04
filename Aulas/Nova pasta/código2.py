# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 11:22:41 2022

@author: Haline Dugolin Ceccato

Projeto desenvolvido na disciplina de Processamento Digital de Imagens - PDI
Aluna especial na Pós Graduação em Ciências da Computação - UNESP
"""

"""
O respectivo programa tem como objetivo reproduzir cinco imagens 
com dimensões 256x256 com 256 níveis de profundidade.

"""

#Para executar o programa é necessário os seguintes pacotes:

import re
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import modEq as eq


'''
Programa construido para obter as matrizes e também gerar as imagens, como 
produto final
'''

'''Os coeficiente m, n e valor,refere-se ao número de colunas, linhas e
número para preenchimento da matriz, respectivamente. Esses dados deverá ser 
fornecido pelo operador. A matriz vazia criada será preenchido após a execução
do programa'''

matriz = [] #declaração de uma matriz vazia
vetor = []

m = eval(input("Defina o número de colunas m:"))
vetor.append(m)
n = eval(input("Defina o número de linhas n:"))
vetor.append(n)
valor = eval(input("Defina o valor de preenchimento valor:"))
vetor.append(valor)

a = eq.cria_matriz(m, n, valor)


imagem = np.array(a)
image = Image.fromarray(imagem)
image.show()
plt.figure(figsize=(256,256))
im = plt.imshow(image, aspect = "auto")
plt.axis("off")
plt.show()



 










        

# c = np.linspace(200, 200, 256)   # início, fim, número de pontos
# c