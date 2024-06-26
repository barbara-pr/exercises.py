import numpy as np
import matplotlib.pyplot as plt

# Construindo gráfico de funções
x = np.linspace(-3, 4, 100)
y = x ** 3 - 2 * x ** 2 + 12 * x - 1
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico da função y = x^3 - 2x^2 + 12x - 1')
plt.grid(True)
plt.show()