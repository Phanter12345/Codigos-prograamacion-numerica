# -*- coding: utf-8 -*-
"""
Created on Mon May 19 18:05:54 2025

@author: Adair
"""

#  Primero intenta leer los datos desde internet (pd.read_csv) si no se lee usa un conjunto de datos de respaldo (StringIO) luego extrae los valores de experiencia y salario y usa np.polyfit para calcular los coeficientes de la recta de mejor ajuste despues se hacen predicciones para 15 30 y 50 años usando la formula de la recta  𝑦 = 𝑚 𝑥 + 𝑏 con matplotlib.pyplot se grafican los datos                           


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

url = 'https://raw.githubusercontent.com/ybfoundation/Dataset/main/Salary_Data.csv'
try:
    df = pd.read_csv(url)
except Exception:
    data = """Experience Years,Salary
1.1,39343
1.2,42774
1.3,46205
1.5,37731
2.0,43525
2.2,39891
2.5,48266
2.9,56642
3.0,60150
3.2,54445
3.2,64445
3.5,60000
3.7,57189
3.8,60200
3.9,63218
4.0,55794
4.0,56957
4.1,57081
4.3,59095
4.5,61111
4.7,64500
4.9,67938
5.1,66029
5.3,83088
5.5,82200
5.9,81363
6.0,93940
6.2,91000
6.5,90000
6.8,91738
7.1,98273
7.9,101302
8.2,113812
8.5,111620
8.7,109431
9.0,105582
9.5,116969
9.6,112635
10.3,122391
10.5,121872
"""
    df = pd.read_csv(StringIO(data))

X = df['Experience Years']
y = df['Salary']
m, b = np.polyfit(X, y, 1)

print(f"Ecuación de regresión: salario = {m:.2f} * años + {b:.2f}")
for exp in [15, 30, 50]:
    print(f"Años={exp}: salario previsto = {m*exp + b:.0f}")

plt.scatter(X, y, color='orange')
line_x = np.array([X.min(), X.max()])
plt.plot(line_x, m*line_x + b, color='red')
plt.xlabel("Años de experiencia")
plt.ylabel("Salario")
plt.show()
