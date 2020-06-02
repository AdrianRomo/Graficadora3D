#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import sys
import math
from mpl_toolkits.mplot3d import Axes3D         # Cargo Axes3D de mpl_toolkits.mplot3d
from scipy.misc import imread                   # Cargo imread de scipy.misc
import numpy as np                              # Cargo numpy como el alias np
import matplotlib.pyplot as plt                 # Cargo matplotlib.pyplot en el alias sp
import os

def cos(n):
    return np.cos(n)

def sen(n):
    return np.sin(n)

def sin(n):
    return np.sin(n)

def tan(n):
    return np.tan(n)

def e(n):
    return np.exp(n)

def sqrt(n):
    return np.sqrt(n)

while 1:
    # Leo una imagen y la almaceno en imagen
    imagen = imread('fondo.jpg')

    # Creo otra figura y la almaceno en figura_3d
    figura_3d = plt.figure()

    # Indicamos que vamos a representar en 3D
    ax = figura_3d.gca(projection = '3d')
    # Creamos los arrays dimensionales de la misma dimension que imagen
    os.system('clear')
    p1 = input('Parametros de X ')
    p2 = input('Parametros de Y ')

    x = np.linspace(-p1, p1, imagen.shape[0])
    y = np.linspace(-p2, p2, imagen.shape[1])
    # Obtenemos las coordenadas a partir de los arrays creados
    x, y = np.meshgrid(x, y)
    # Defino la funcion que deseo representar
    R = input('Inserte una funcion F(X,Y): ')

    Z = R

    # Reescalamos de RGB a [0-1]
    imagen = imagen.swapaxes(0, 1) / 255.

    # meshgrid orienta los ejes al reves luego hay que voltear
    ax.plot_surface(x, y, Z, facecolors = np.flipud(imagen))

    # Fijamos la posicion inicial de la grafica
    ax.view_init(45, -35)

    # Anadimos etiquetas
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    ax.set_zlabel('Eje Z')

    # Mostramos en pantalla
    plt.show()
    #Salida
    salida = raw_input('Presione enter para salir o alguna otra tecla para seguir graficando')
    if salida == "":
        sys.exit(1)
