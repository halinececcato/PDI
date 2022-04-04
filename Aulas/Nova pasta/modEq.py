# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 23:45:12 2022

@author: Haline Dugolin Ceccato
"""

'''O presente arquivo foi desenvolvido ao longo da disciplina de:
    Processamento Digital de Imagens, realizado como aluna especial no 
    Programa de Pós Graduação em Ciência da Computação na UNESP
    '''
'''Neste arquivo contém o modulo utilizado para o desenvolvimento do programa
que permite obter cinco imagens com dimensões 256x256 com 256 níveis de 
profundidade'''


matriz = [] #matriz vazia que será preenchida
def cria_matriz(m, n, valor): #número de linhas, números de colunas, valor de preenchimento
    for i in range(m):
        linha = []
        for j in range(n):
            linha.append(valor)
        matriz.append(linha)
    return matriz

imagem = np.array(a)
image = Image.fromarray(imagem)
image.show()
plt.figure(figsize=(256,256))
im = plt.imshow(image, aspect = "auto")
plt.axis("off")
plt.show()
