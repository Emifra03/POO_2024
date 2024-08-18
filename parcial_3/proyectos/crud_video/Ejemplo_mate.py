import math
import matplotlib.pyplot as plt
import numpy as np

def funcion(x):
    return math.sin(x)

x = np.linspace(0, 2 * math.pi, 100)

y = [funcion(i) for i in x]

plt.plot(x, y, label='sin(x)')

plt.title('Gráfica de la función sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()

plt.show()
