import numpy as np

# Subtração entre dois arrays
print('Subtraindo arrays:')
v = np.array([[22, 12, 54, 89, 11]])
u = np.array([[18, 4, 39, 61, 8]])
m = v - u
print(m)

print('-' * 15)

# Multiplicação entre dois arrays
print('Multiplicando arrays:')
notas = np.array([[90, 85, 70, 100]])
pesos = np.array([[0.2, 0.2, 0.3, 0.3]])
media = np.inner(notas, pesos)
print(media)