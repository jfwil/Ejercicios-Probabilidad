import math

#Distribucion de poisson
print("Distribución de poisson")

#Datos
lambda_km = 0.2    
km = 5
lmbda = lambda_km * km 

#a) P(X = 0)
P0 = math.exp(-lmbda) * (lmbda**0) / math.factorial(0)

#b) P(X ≥ 2) = 1 - [P(0) + P(1)] 
P1 = math.exp(-lmbda) * (lmbda**1) / math.factorial(1)
P_ge2 = 1 - (P0 + P1)

#c) Esperanza
esperanza = lmbda

#Resultados
print("P(X = 0):", round(P0, 4))
print("P(X ≥ 2):", round(P_ge2, 4))
print("Esperanza E[X]:", esperanza)

#Distribución normal

print("Distribución de normal")

#Datos
mu = 170
sigma = 6

# P(165 < X < 180) = Φ((180-μ)/σ) - Φ((165-μ)/σ)
P_165_180 = norm.cdf(180, mu, sigma) - norm.cdf(165, mu, sigma)

print("\n=== Distribución Normal ===")
print("P(165 < X < 180):", round(P_165_180, 4))