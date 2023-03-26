import matplotlib.pyplot as plt
import numpy as np
import math
x=np.linspace(1,100,100)
def f(x): return (-1)*math.log10(x)

f2=np.vectorize(f)
plt.plot(x,f2(x), 'bo')
plt.show()
