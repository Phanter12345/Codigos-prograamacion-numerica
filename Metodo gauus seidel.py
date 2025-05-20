# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 23:09:30 2025

@author: Adair
"""

import numpy as np

A = np.array([[1, -0.1, -0.2],
              [0.1, 7, -0.3],
              [0.3, -0.2, -10]], dtype=float)
b = np.array([7.85, 19.3, 71.4], dtype=float)

n = len(b)
x = np.zeros(n)
print("\nJacobi - Iteracion 0:", x)

for k in range(3):
    x_nuevo = np.zeros(n)
    for i in range(n):
        suma = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i+1:], x[i+1:])
        x_nuevo[i] = (b[i] - suma) / A[i, i]
    x = x_nuevo
    print(f"Jacobi - Iteracion {k+1}:", x)

x = np.zeros(n)
print("\nGauss-Seidel - Iteracion 0:", x)

for k in range(3):
    for i in range(n):
        suma = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i+1:], x[i+1:])
        x[i] = (b[i] - suma) / A[i, i]
    print(f"Gauss-Seidel - Iteracion {k+1}:", x)
