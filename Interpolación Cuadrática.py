# -*- coding: utf-8 -*-
"""
Created on Mon May 19 17:46:13 2025

@author: Adair
"""

import matplotlib.pyplot as plt
import numpy as np

x = [2, 3, 5]
y = [6, 19, 99]

b0 = y[0]
b1 = (y[1] - y[0]) / (x[1] - x[0])
b2 = ((y[2] - y[1]) / (x[2] - x[1]) - b1) / (x[2] - x[0])

f4 = b0 + b1 * (4 - x[0]) + b2 * (4 - x[0]) * (4 - x[1])
print(f"{f4:.2f}")

xp = np.linspace(1, 8, 100)
yp = [b0 + b1 * (xi - x[0]) + b2 * (xi - x[0]) * (xi - x[1]) for xi in xp]

plt.scatter([1, 2, 3, 5, 7, 8], [3, 6, 19, 99, 291, 444], color='red')
plt.plot(xp, yp, linestyle='--')
plt.scatter([4], [f4], color='blue')
plt.show()
