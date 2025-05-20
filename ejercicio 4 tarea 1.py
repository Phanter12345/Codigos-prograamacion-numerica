# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 19:42:23 2025

@author: Adair
"""

import random

#N = int(input("Introduce un numero entero y positivo: "))

N = 3
if N > 0:
    
    v= [random.randint(1, 9) for _ in range(N)]
    print("vector :", v)
    

    M = [[v[i] * (j + 1) for i in range(N)] for j in range(N)]
    
    print("matriz de multiplos por columnas:")
    for fila in M:
        print(fila)
else:
    print("Error")