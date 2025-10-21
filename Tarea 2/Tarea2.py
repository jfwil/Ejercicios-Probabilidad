import itertools
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

#Lanzamiento de 2 dados justos

#Datos 
dados = [1, 2, 3, 4, 5, 6]
espacio_muestral = list(itertools.product(dados, repeat=2))

#Probabilidad conjunta de cada par (x, y)
prob_conjunta = {par: 1/36 for par in espacio_muestral}

#Suma de los dos dados
sumas = [x + y for x, y in espacio_muestral]

#Función de probabilidad (PMF) de la suma
valores, conteos = np.unique(sumas, return_counts=True)
pmf = conteos / 36  # cada suma tiene cierta frecuencia sobre 36 posibles

#Función de probabilidad acumulativa
cdf = np.cumsum(pmf)

#Valor medio o esperanza
valor_medio = np.sum(valores * pmf)

#Resultados 
print("Función de probabilidad conjunta (cada par tiene prob. 1/36):")
print(prob_conjunta)
print("\nFunción de probabilidad acumulativa (CDF):")
for v, p in zip(valores, cdf):
    print(f"P(X ≤ {v}) = {p:.4f}")
print("\nValor medio (esperanza):", valor_medio)

#Gráfica de la PMF y la CDF
plt.figure(figsize=(8,4))

plt.subplot(1,2,1)
plt.bar(valores, pmf, color='skyblue', edgecolor='black')
plt.title("Función de probabilida")
plt.xlabel("Suma de los 2 dados")
plt.ylabel("P(X = x)")

plt.subplot(1,2,2)
plt.step(valores, cdf, where='mid', color='orange')
plt.title("Función de probabilidad acumulada")
plt.xlabel("Suma de los 2 dados")
plt.ylabel("P(X ≤ x)")

plt.tight_layout()
plt.show()

#SEGUNDO PUNTO

print("Segundo Punto")

#Variable y constante
x, k = sp.symbols('x k', real=True, positive=True)

#Definición de la función
f = k * x

#Encontrar k para que la función sea de densidad
k_val = sp.solve(sp.integrate(f, (x, 0, 6)) - 1, k)[0]

#Sustituir k en la función
f = f.subs(k, k_val)

#Calculo de probabilidades
P_total = sp.integrate(f, (x, 0, 6))
E = sp.integrate(x * f, (x, 0, 6))
E2 = sp.integrate(x**2 * f, (x, 0, 6))
Var = E2 - E**2

#Resultados
print("Constante k:", float(k_val))
print("Probabilidad P(0 ≤ X < 6):", float(P_total))
print("Valor esperado E[X]:", float(E))
print("Varianza Var(X):", float(Var))