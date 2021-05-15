import matplotlib.pyplot as plt 
import numpy as np
from scipy import signal
import math

t=np.arange(-5,5,0.1)

def x(t):
    y=5*math.e**(-2*t-3)
    return y
v0=x(4-t)
v1=x(t/8+2)

plt.subplot(211)
plt.plot(t,v0)
plt.subplot(212)
plt.plot(t,v1)

plt.show()
