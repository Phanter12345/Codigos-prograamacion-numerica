# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 19:03:52 2025

@author: Adair
"""
import random  

#N = int(input("Introduce un numero entero y positivo: "))
N = 6
if N > 0:
    v = [random.randint(1, 9) for _ in range(N)]
    print("vector :", v)
else:
    print("Error")
