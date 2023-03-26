import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-3,3,50)
def f(x): return x**2

plt.plot(x,f(x), 'bo')

plt.show()
