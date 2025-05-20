# -*- coding: utf-8 -*-
"""
Created on Mon May 19 17:49:41 2025

@author: Adair
"""
import matplotlib.pyplot as plt
import numpy as np

# El resultado que imprime esta mal da 44 y debe dar 57 creo que el problema esta en ese enredadedro de operaciones alguna no se debe estar efectuando bien

x = [1, 2, 3, 5, 7]
y = [3, 6, 19, 99, 291]

a0 = y[0]
a1 = (y[1] - y[0]) / (x[1] - x[0])
a2 = (((y[2] - y[1]) / (x[2] - x[1])) - a1) / (x[2] - x[0])
a3 = ((((y[3] - y[2]) / (x[3] - x[2])) - ((y[2] - y[1]) / (x[2] - x[1]))) / (x[3] - x[1]) - a2) / (x[3] - x[0])
a4 = (((((y[4] - y[3]) / (x[4] - x[3])) - ((y[3] - y[2]) / (x[3] - x[2]))) / (x[4] - x[2]) - 
      (((y[3] - y[2]) / (x[3] - x[2])) - ((y[2] - y[1]) / (x[2] - x[1]))) / (x[3] - x[1])) - a3) / (x[4] - x[0])

def f4(xi):
    return (a0 
            + a1*(xi - x[0]) 
            + a2*(xi - x[0])*(xi - x[1]) 
            + a3*(xi - x[0])*(xi - x[1])*(xi - x[2]) 
            + a4*(xi - x[0])*(xi - x[1])*(xi - x[2])*(xi - x[3]))

f4_val = f4(4)
print(f"{f4_val:.2f}")

xp = np.linspace(1, 8, 100)
yp = [f4(i) for i in xp]

plt.scatter([1, 2, 3, 5, 7], y, color='red')
plt.plot(xp, yp, linestyle='--')
plt.scatter([4], [f4_val], color='blue')
plt.show()

