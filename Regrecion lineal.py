# -*- coding: utf-8 -*-
"""
Created on Mon May 19 17:33:23 2025

@author: Adair
"""
import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5, 6]
y = [5.04, 8.12, 10.64, 13.18, 16.20, 20.04]

n = len(x)
a1 = (n * sum(xi * yi for xi, yi in zip(x, y)) - sum(x) * sum(y)) / (n * sum(xi**2 for xi in x) - sum(x)**2)
a0 = (sum(y) - a1 * sum(x)) / n

print(f"f(x) = {a0:.4f} + {a1:.4f}x")

for xi in [15, 30, 50]:
    print(f"f({xi}) = {a0 + a1 * xi:.2f}")

xp = np.linspace(0, 7, 100)
yp = a0 + a1 * xp

plt.scatter(x, y, color='red')
plt.plot(xp, yp, linestyle='--')
plt.show()

