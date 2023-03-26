import matplotlib.pyplot as plt
import numpy as np
import math
x=[1,10,100,1000,10000]
def f(x): return math.log(x,10)
def g(x): return x
f2=np.vectorize(f)
g2=np.vectorize(g)
plt.plot(x,f2(x), 'bo')
#plt.plot(x,g2(x), 'b+')
plt.show()
