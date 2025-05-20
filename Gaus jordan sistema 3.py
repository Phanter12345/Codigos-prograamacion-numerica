# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 22:59:17 2025

@author: Adair
"""

import numpy as np

A = np.array([[1, 2, 1], [3, 8, 1], [0, 4, 1]], dtype=float)
b = np.array([2, 12, 2], dtype=float)

M = np.column_stack((A, b))

n = len(b)
for i in range(n):
    if M[i, i] == 0:
        for j in range(i + 1, n):
            if M[j, i] != 0:
                M[[i, j]] = M[[j, i]]
                break
    M[i] /= M[i, i]
    for j in range(n):
        if i != j:
            M[j] -= M[j, i] * M[i]

print("Solución (Gauss-Jordan):", M[:, -1])

print("Solución (Matriz Inversa):", np.linalg.inv(A) @ b)

det_A = np.linalg.det(A)
print("Solución (Cramer):", [np.linalg.det(np.column_stack((A[:, :i], b, A[:, i+1:]))) / det_A for i in range(n)])

L = np.zeros((n, n))
U = np.zeros((n, n))
for i in range(n):
    L[i, i] = 1
    for j in range(i, n):
        U[i, j] = A[i, j] - sum(L[i, k] * U[k, j] for k in range(i))
    for j in range(i + 1, n):
        L[j, i] = (A[j, i] - sum(L[j, k] * U[k, i] for k in range(i))) / U[i, i]

print("Solución (LU):", np.linalg.solve(U, np.linalg.solve(L, b)))



