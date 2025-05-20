# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 22:50:18 2025

@author: Adair
"""

import numpy as np

A = np.array([[4, -2, 1], [-2, 4, -2], [1, -2, 4]], dtype=float)
b = np.array([11, -16, 17], dtype=float)

M = np.column_stack((A, b))
n = len(b)

for i in range(n):
    if M[i, i] == 0:
        for j in range(i + 1, n):
            if M[j, i] != 0:
                M[[i, j]] = M[[j, i]]
                break
    M[i] = M[i] / M[i, i]
    for j in range(n):
        if i != j:
            M[j] = M[j] - M[j, i] * M[i]

print(M[:, -1])

A_inv = np.linalg.inv(A)
print(A_inv @ b)

det_A = np.linalg.det(A)
solucion = []
for i in range(len(b)):
    Ai = A.copy()
    Ai[:, i] = b
    solucion.append(np.linalg.det(Ai) / det_A)
print(solucion)

L = np.zeros((n, n))
U = np.zeros((n, n))
for i in range(n):
    L[i, i] = 1
    for j in range(i, n):
        U[i, j] = A[i, j] - sum(L[i, k] * U[k, j] for k in range(i))
    for j in range(i + 1, n):
        L[j, i] = (A[j, i] - sum(L[j, k] * U[k, i] for k in range(i))) / U[i, i]

print(L)
print(U)

