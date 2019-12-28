import numpy as np
import matplotlib.pyplot as plt

r = np.linspace(0,100,1000)
m=10
def r1(r,a):
    return -r + a;

def r2(r,a):
    return (r-2*m)/(r+2*m) +a;

plt.plot(r,r1(r,0))
plt.plot(r,r2(r,0))
plt.show
