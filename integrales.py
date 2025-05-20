# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 21:34:10 2025

@author: Adair
"""
import numpy as np
from sympy import symbols, integrate, cos, exp, pi

def f1(x): return 2 * np.cos(2 * x)
def f2(x): return -x**2 - x/2 + 4
def f3(x): return np.exp(-x**2)

x = symbols('x')
analytical = [
    integrate(2 * cos(2 * x), (x, 0, pi/4)),
    integrate(-x**2 - x/2 + 4, (x, 0.5, 1.5)),
    integrate(exp(-x**2), (x, 0, 1))
]

print("=== RESULTADOS ANALÍTICOS ===")
for i, a in enumerate(analytical):
    print(f"Integral {i+1}: {a.evalf():.6f}")

def trap_simple(f, a, b):
    return (b - a) / 2 * (f(a) + f(b))

def trap_multiple(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    s = f(a) + f(b)
    for i in range(1, n):
        s += 2 * f(x[i])
    return h / 2 * s

def simpson_13(f, a, b):
    m = (a + b) / 2
    return (b - a) / 6 * (f(a) + 4 * f(m) + f(b))

def simpson_38(f, a, b):
    h = (b - a) / 3
    return 3 * h / 8 * (f(a) + 3 * f(a + h) + 3 * f(a + 2 * h) + f(b))

def simpson_68(f, a, b):
    n = 6
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    s = f(x[0]) + f(x[6]) + 5 * (f(x[1]) + f(x[5])) + 6 * f(x[3]) + f(x[2]) + f(x[4])
    return 3 * h / 10 * s

functions = [f1, f2, f3]
limits = [(0, np.pi/4), (0.5, 1.5), (0, 1)]

methods = [
    ("Trapecio simple", trap_simple),
    ("Trapecio n=2", lambda f, a, b: trap_multiple(f, a, b, 2)),
    ("Trapecio n=4", lambda f, a, b: trap_multiple(f, a, b, 4)),
    ("Trapecio n=6", lambda f, a, b: trap_multiple(f, a, b, 6)),
    ("Simpson 1/3", simpson_13),
    ("Simpson 3/8", simpson_38),
    ("Simpson 6/8", simpson_68)
]

print("\n=== RESULTADOS NUMÉRICOS ===")
for i in range(3):
    f = functions[i]
    a, b = limits[i]
    print(f"\nFunción {i+1} en [{a}, {b}]:")
    for name, method in methods:
        result = method(f, a, b)
        if i == 2:
            print(f"{name}: {result:.6f} | Error: N/A")
        else:
            exact = float(analytical[i])
            error = abs((exact - result) / exact * 100)
            print(f"{name}: {result:.6f} | Error: {error:.2f}%")

