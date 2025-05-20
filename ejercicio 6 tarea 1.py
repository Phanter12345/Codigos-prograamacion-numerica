# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 22:11:58 2025

@author: Adair
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)


plt.plot(x, np.sin(x), label="sin(x)")  #funcion seno

plt.plot(x, np.cos(x), label="cos(x)")   #funcion coseno

plt.plot(x, np.tan(x), label="tan(x)")   #funcion tangente


plt.ylim(-10, 10)  

plt.xlabel("x")

plt.ylabel("y")

plt.title("Funciones sin(x), cos(x) y tan(x)")

plt.legend()

plt.grid(True)

plt.show()
