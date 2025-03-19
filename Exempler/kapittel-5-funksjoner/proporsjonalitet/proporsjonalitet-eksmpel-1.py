import matplotlib.pyplot as plt
import numpy as np

def direkte_proporsjonalitet(x, k):
    return k * x

x = np.linspace(0, 10, 100)
k = 2  # Konstanten k
y = direkte_proporsjonalitet(x, k)

plt.plot(x, y, label=f'y = {k}x')
plt.title('Direkte proporsjonalitet')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

def omvendt_proporsjonalitet(x, k):
    return k / x

x = np.linspace(1, 10, 100)  # Unngå x = 0 for å unngå deling på null
k = 5  # Konstanten k
y = omvendt_proporsjonalitet(x, k)

plt.plot(x, y, label=f'y = {k}/x')
plt.title('Omvendt proporsjonalitet')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()