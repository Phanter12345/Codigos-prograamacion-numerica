# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 19:34:26 2025

@author: Adair
"""

import random

#N = int(input("Introduce un numero entero y positivo: "))

N=3
if N > 0:
   
    v = [random.randint(1, 9) for _ in range(N)]
    
    print("vector :", v)
    
   
    
   
    
    M = [[v[j] * (i + 1) for j in range(N)] for i in range(N)]
    
    
    print("Matriz de multiplos por filas:")
    
    for fila in M:
        
        print(fila)
        
else:
    
    print("Error")