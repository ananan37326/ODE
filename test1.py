import numpy as np
from math import sin
import matplotlib.pyplot as plt

def func(x,y):
    return (x+20*y) * sin(x*y)

def Euler(x,h):
    n = len(x)
    y = np.zeros(n)
    y[0] = 4
    for i in range(0,n-1):
        y[i+1] = y[i] + func(x[i],y[i]) * h
    return y

def Heun(x,h):
    n = len(x)
    y0 = np.zeros(n)
    y = np.zeros(n)
    y[0] = 4
    for i in range(0, n - 1):
        y0[i+1] = y[i] + func(x[i],y[i]) * h
        y[i+1] = y[i] + 0.5 * (func(x[i],y[i]) + func(x[i+1],y0[i+1])) * h
    return y

step = 0.01
x1 = np.arange(0,10+step,step=step)
x1 = np.around(x1,decimals=2)

y1 = Heun(x1,step)

step = 0.05
x2 = np.arange(0,10+step,step=step)
x2 = np.around(x2,decimals=2)
y2 = Heun(x2,step)

step = 0.1
x3 = np.arange(0,10+step,step=step)
x3 = np.around(x3,decimals=2)
y3 = Heun(x3,step)

step = 0.5
x4 = np.arange(0,10+step,step=step)
x4 = np.around(x4,decimals=2)
y4 = Heun(x4,step)


plt.plot(x1,y1,linestyle='-',marker='.',color='red',label='Step Size 0.01')
plt.plot(x2,y2,linestyle='-',marker='.',color='blue',label='Step Size 0.05')
plt.plot(x3,y3,linestyle='-',marker='.',color='green',label='Step Size 0.1')
plt.plot(x4,y4,linestyle='-',marker='.',color='yellow',label='Step Size 0.5')
plt.grid()
plt.legend()
plt.show()

