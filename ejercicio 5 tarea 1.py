# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 19:47:01 2025

@author: Adair
"""

import random

def Fila(N):
    v = [random.randint(1, 9) for _ in range(N)]
    print("Vector fila:", v)
    matriz = [[v[j] * (i + 1) for j in range(N)] for i in range(N)]
    print("Matriz  filas:")
    for fila in matriz:
        print(fila)

def columna(N):
    ve = [random.randint(1, 9) for _ in range(N)]
    print("Vector columna:", ve)
    matriz = [[ve[i] * (j + 1) for i in range(N)] for j in range(N)]
    print("Matriz  columnas:")
    for fila in matriz:
        print(fila)

# N = int(input("Introduce un numero entero y positivo: "))
N = 4
if N > 0:
    Fila(N)
    columna(N)
else:
    print("Error")