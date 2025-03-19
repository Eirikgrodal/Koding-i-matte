import matplotlib.pyplot as plt
import numpy as np

# Lineær funksjon
def lineær_funksjon(x):
    return 3 * x - 2

x = np.linspace(-10, 10, 400)
y = lineær_funksjon(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Lineær: 3x - 2')
plt.title('Lineær funksjon')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

# Kvadratisk funksjon
def kvadratisk_funksjon(x):
    return x**2 - 4 * x + 4

x = np.linspace(-10, 10, 400)
y = kvadratisk_funksjon(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Kvadratisk: x^2 - 4x + 4')
plt.title('Kvadratisk funksjon')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

# Eksponentialfunksjon
def eksponential_funksjon(x):
    return np.exp(x)

x = np.linspace(-2, 2, 400)
y = eksponential_funksjon(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Eksponential: e^x')
plt.title('Eksponentialfunksjon')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()