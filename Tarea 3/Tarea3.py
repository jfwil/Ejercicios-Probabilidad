import math
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

#Datos
sistemas = 3
electronica = 2
industrial = 3
total = sistemas + electronica + industrial
n = 2  # seleccionados

#Función de probabilidad conjunta
def fxy(x, y):
    if x + y <= n:
        return (math.comb(sistemas, x) * math.comb(electronica, y) *
                math.comb(industrial, n - x - y)) / math.comb(total, n)
    return 0

#Calcular todos los valores posibles
x_vals = range(0, n + 1)
y_vals = range(0, n + 1)
Z = np.array([[fxy(x, y) for y in y_vals] for x in x_vals])

#Mostrar tabla de probabilidades
for i, x in enumerate(x_vals):
    for j, y in enumerate(y_vals):
        if Z[i, j] > 0:
            print(f"f({x},{y}) = {Z[i,j]:.4f}")

#Gráfica 3D
X, Y = np.meshgrid(x_vals, y_vals)
fig = plt.figure(figsize=(6,5))
ax = fig.add_subplot(111, projection='3d')
ax.bar3d(X.ravel(), Y.ravel(), np.zeros_like(Z).ravel(), 0.3, 0.3, Z.ravel(), color='skyblue', edgecolor='black')
ax.set_xlabel('X (Sistemas)')
ax.set_ylabel('Y (Electrónica)')
ax.set_zlabel('f(x, y)')
ax.set_title('Función de Probabilidad Conjunta f(x, y)')
plt.show()

#fabrica de chocolate

#Variables
x, y = sp.symbols('x y', real=True, nonnegative=True)

#Definición de la función f(x,y)
f = (2/5) * (2*x + 3*y)

#1.Verificacion función de probabilidad conjunta
integral_total = sp.integrate(sp.integrate(f, (x, 0, 1)), (y, 0, 1))

#2.resultado 
print("∬ f(x,y) dxdy =", float(integral_total))

#3.Grafica de la función f(x,y)
x_vals = np.linspace(0, 1, 50)
y_vals = np.linspace(0, 1, 50)
X, Y = np.meshgrid(x_vals, y_vals)
Z = (2/5) * (2*X + 3*Y)

fig = plt.figure(figsize=(6,5))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='plasma', edgecolor='none', alpha=0.8)
ax.set_title("Función de densidad conjunta f(x,y)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("f(x,y)")
plt.show()