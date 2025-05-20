# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 22:55:52 2025

@author: Adair
"""

import numpy as np

A = np.array([[1, 1, 1], [1, 2, 5], [1, 4, 25]], dtype=float)
b = np.array([6, 12, 36], dtype=float)

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

print("Sistema 2 - Solución (Gauss-Jordan):", M[:, -1])

solucion = np.linalg.inv(A) @ b
print("Sistema 2 - Solución (Matriz Inversa):", solucion)

det_A = np.linalg.det(A)
solucion = []
for i in range(n):
    Ai = A.copy()
    Ai[:, i] = b
    solucion.append(np.linalg.det(Ai) / det_A)

print("Sistema 2 - Solución (Cramer):", solucion)

L = np.zeros((n, n))
U = np.zeros((n, n))
for i in range(n):
    L[i, i] = 1
    for j in range(i, n):
        U[i, j] = A[i, j] - sum(L[i, k] * U[k, j] for k in range(i))
    for j in range(i + 1, n):
        L[j, i] = (A[j, i] - sum(L[j, k] * U[k, i] for k in range(i))) / U[i, i]

print("Sistema 2 - L:\n", L)
print("Sistema 2 - U:\n", U)

z = np.linalg.solve(L, b)
x = np.linalg.solve(U, z)
print("Sistema 2 - Solución (LU):", x)


