import math
from math import factorial

# PRIMER PUNTO
print("PRIMER PUNTO")
#Datos Iniciales
industrial = 9
sistemas = 3
electronica = 8
total = industrial + sistemas + electronica
r = 3

#Probabilidad de que los 3 estudiantes sean de electronica

#Probabilidad mediante combinaciones
comb_total = math.comb(total, r)
comb_favorable = math.comb(electronica, r)
prob_combinacion = comb_favorable / comb_total

#Probabilidad mediante permutaciones 
perm_total = math.perm(total, r)
perm_favorable = math.perm(electronica, r)
prob_permutacion = perm_favorable / perm_total

#Probabilidad mediante sustitucion
p_electronica = electronica / total
prob_sustitucion = p_electronica ** r

#Resultados
print("Probabilidad de que los 3 sean de electronica")
print("Probabilidad por COMBINACIÓN:", prob_combinacion)
print("Probabilidad por PERMUTACIÓN:", prob_permutacion)
print("Probabilidad por SUSTITUCIÓN:", prob_sustitucion)

#Probabilidad de que los 3 estudiantes sean de sistemas

#Probabilidad mediante combinaciones
comb_total = math.comb(total, r)
comb_favorable = math.comb(sistemas, r)
prob_combinacion = comb_favorable / comb_total

#Probabilidad mediante permutaciones
perm_total = math.perm(total, r)
perm_favorable = math.perm(sistemas, r)
prob_permutacion = perm_favorable / perm_total

#Probabilidad mediante sustitucion
p_sistemas = sistemas / total
prob_sustitucion = p_sistemas ** r

#Resultados
print("Probabilidad de que los 3 sean de sistemas")
print("Probabilidad por COMBINACIÓN:", prob_combinacion)
print("Probabilidad por PERMUTACIÓN:", prob_permutacion)
print("Probabilidad por SUSTITUCIÓN:", prob_sustitucion)

#Probabilidad de que 2 sean de electronica y 1 de sistemas

#Probabilidad mediante combinaciones
comb_total = math.comb(total, r)
comb_favorable = math.comb(electronica, 2) * math.comb(sistemas, 1)
prob_combinacion = comb_favorable / comb_total

#Probabilidad mediante permutaciones
perm_total = math.perm(total, r)
perm_favorable = math.perm(electronica, 2) * math.perm(sistemas, 1)
prob_permutacion = perm_favorable / perm_total

#Probabilidad mediante sustitucion
p_electronica = electronica / total
p_sistemas = sistemas / total
prob_sustitucion = (p_electronica ** 2) * p_sistemas

#Resultados
print("Probabilidad de que 2 sean de electronica y 1 de sistemas")
print("Probabilidad por COMBINACIÓN:", prob_combinacion)
print("Probabilidad por PERMUTACIÓN:", prob_permutacion)
print("Probabilidad por SUSTITUCIÓN:", prob_sustitucion)

#Probabilidad de que sea elegido un estudiante de cada carreara

#Probabilidad mediante combinaciones
comb_total = math.comb(total, r)
comb_favorable = math.comb(industrial, 1) * math.comb(sistemas, 1) * math.comb(electronica, 1)
prob_combinacion = comb_favorable / comb_total

#Probabilidad mediante permutaciones
perm_total = math.perm(total, r)
perm_favorable = math.perm(industrial, 1) * math.perm(sistemas, 1) * math.perm(electronica, 1)
prob_permutacion = perm_favorable / perm_total

#Probabilidad mediante sustitucion
p_industrial = industrial / total
p_sistemas = sistemas / total
p_electronica = electronica / total
prob_sustitucion = p_industrial * p_sistemas * p_electronica

#Resultados
print("Probabilidad de que se elijan un estudiante de cada carrera")
print("Probabilidad por COMBINACIÓN:", prob_combinacion)
print("Probabilidad por PERMUTACIÓN:", prob_permutacion)
print("Probabilidad por SUSTITUCIÓN:", prob_sustitucion)

#SEGUNDO PUNTO
print("SEGUNDO PUNTO")
#A. De cuantas maneras se pueden organizar 4I, 6E y 2S

industrial = 4
electrica = 6
sistemas = 2
total = industrial + electrica + sistemas

maneras = factorial(total) // (factorial(industrial) * factorial(electrica) * factorial(sistemas))

print(f"Se pueden organizar de {maneras} maneras diferentes")

#B.

manerasB = factorial(industrial) * factorial(9)

print(f"Se pueden organizar de {manerasB} maneras diferentes")