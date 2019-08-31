import numpy as np
import matplotlib.pyplot as plt
from math import sin

def func(x,y):
    return (x+20*y) * sin(x*y)

def Euler(x,h):
    n = len(x)
    y = np.zeros(n)
    y[0] = 4
    for i in range(0,n-1):
        y[i+1] = y[i] + func(x[i],y[i]) * h
    return y

def RK2(x,h,a2):
    a1 = 1 - a2
    p1 = 0.5 / a2
    q11 = 0.5 / a2

    n = len(x)
    y = np.zeros(n)
    y[0] = 4
    for i in range(0, n - 1):
        k1 = func(x[i],y[i])
        k2 = func(x[i]+p1*h,y[i]+q11*k1*h)
        y[i+1] = y[i] + (a1*k1 + a2*k2) *h
    return y

def Heun(x,h):
    a2 = 1/2
    y = RK2(x,h,a2)

    return y

def Midpoint(x,h):
    a2 = 1
    y = RK2(x,h,a2)

    return y

def Ralston(x,h):
    a2 = 2/3
    y = RK2(x,h,a2)

    return y

def RK4(x,h):
    n = len(x)
    y = np.zeros(n)
    y[0] = 4
    a = 1 / 6
    for i in range(0, n - 1):
        k1 = func(x[i], y[i])
        k2 = func(x[i] + 0.5 * h, y[i] + 0.5 * k1 * h)
        k3 = func(x[i] + 0.5 * h, y[i] + 0.5 * k2 * h)
        k4 = func(x[i] + h, y[i] + k3 * h)
        y[i + 1] = y[i] + (k1 + 2 * k2 + 2 * k3 + k4) * h * a
    return y

xi = 0
xf = 10
steps = [0.01,0.05,0.1,0.5]
colors = ['red','blue','green','yellow','cyan']

#Euler
plt.figure(figsize=(6,6))
plt.title("Euler Method")
plt.xlabel("x values")
plt.ylabel("y values")
for i in range(4):
    x = np.arange(xi,xf+steps[i],step=steps[i])
    x = np.around(x,decimals=2)
    y = Euler(x,steps[i])
    plt.plot(x,y,color=colors[i],marker='.',label="Step Size"+str(steps[i]))
plt.grid()
plt.legend()
plt.show()

#Heun
plt.figure(figsize=(6,6))
plt.title("Heun Method")
plt.xlabel("x values")
plt.ylabel("y values")
for i in range(4):
    x = np.arange(xi,xf+steps[i],step=steps[i])
    x = np.around(x,decimals=2)
    y = Heun(x,steps[i])
    plt.plot(x,y,color=colors[i],marker='.',label="Step Size"+str(steps[i]))
plt.grid()
plt.legend()
plt.show()

#Midpoint
plt.figure(figsize=(6,6))
plt.title("Midpoint Method")
plt.xlabel("x values")
plt.ylabel("y values")
for i in range(4):
    x = np.arange(xi,xf+steps[i],step=steps[i])
    x = np.around(x,decimals=2)
    y = Midpoint(x,steps[i])
    plt.plot(x,y,color=colors[i],marker='.',label="Step Size"+str(steps[i]))
plt.grid()
plt.legend()
plt.show()

#Ralston
plt.figure(figsize=(6,6))
plt.title("Ralston Method")
plt.xlabel("x values")
plt.ylabel("y values")
for i in range(4):
    x = np.arange(xi,xf+steps[i],step=steps[i])
    x = np.around(x,decimals=2)
    y = Ralston(x,steps[i])
    plt.plot(x,y,color=colors[i],marker='.',label="Step Size"+str(steps[i]))
plt.grid()
plt.legend()
plt.show()

#RK4
plt.figure(figsize=(6,6))
plt.title("RK4 Method")
plt.xlabel("x values")
plt.ylabel("y values")
for i in range(4):
    x = np.arange(xi,xf+steps[i],step=steps[i])
    x = np.around(x,decimals=2)
    y = RK4(x,steps[i])
    plt.plot(x,y,color=colors[i],marker='.',label="Step Size"+str(steps[i]))
plt.grid()
plt.legend()
plt.show()

#Steps
names = ["Euler","Heun","Midpoint","Ralston","RK4"]

for i in range(4):
    plt.figure(figsize=(6,6))
    plt.title("Step Size"+str(steps[i]))
    plt.xlabel("x values")
    plt.ylabel("y values")
    x = np.arange(xi,xf+steps[i],step=steps[i])
    x = np.around(x,decimals=2)
    y = []
    y1 = Euler(x,steps[i])
    y2 = Heun(x,steps[i])
    y3 = Midpoint(x,steps[i])
    y4 = Ralston(x,steps[i])
    y5 = RK4(x,steps[i])

    plt.plot(x, y1, color=colors[0],  label=names[0])
    plt.plot(x, y2, color=colors[1],  label=names[1])
    plt.plot(x, y3, color=colors[2],  label=names[2])
    plt.plot(x, y4, color=colors[3],  label=names[3])
    plt.plot(x, y5, color=colors[4],  label=names[4])

    plt.grid()
    plt.legend()
    plt.show()