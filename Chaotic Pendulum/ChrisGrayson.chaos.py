from numpy import *
from scipy import *
from pylab import *
from matplotlib import pyplot as plt
import numpy as np
#Chris Grayson

#Created on Mon Mar 23 20:03:20 2015

#Equation of motion
    #q'' + 2*B*q' + (wo)**2*sin(q) = Y*(wo)**2*cos(w*t)
#Constants
#B = b/(2*m) = 0.25*wo
#Y = Fo/(m*g)
#w = 2*pi
#wo= 1.5*w
#Constant
w = 2.0*math.pi
wo = 1.5*w
B = 0.25*wo
#x = q
#x' = q'
#y = q'
#y' = q''
#x' = y
#y' = Y*(wo)**2*cos(w*t) - 2*B*y  - (wo)**2*sin(x)

Y=0.2

def RK4(f, ti, yi, dt):
    k1 = dt*f(ti,          yi)
    k2 = dt*f(ti + 0.5*dt, yi + 0.5*k1)
    k3 = dt*f(ti + 0.5*dt, yi + 0.5*k2)
    k4 = dt*f(ti + dt    , yi + k3)
    yf = yi +(1./6.)*(k1 + 2.*k2 + 2.*k3 + k4)
    return yf
    
def func(t,y):
    return array([y[1], Y*(wo)**2*cos(w*t)- 2*B*y[1]-(wo)**2*sin(y[0])])
    
w = 2.0*math.pi
wo = 1.5*w
B = 0.25*wo
 
 
t = 0.0
dt = 0.01
y = array([0.0 , 0.0])
t1list = [t]
y1list = [y[0]]
#Figure 12.2 
for i in range(600):
    Y = 0.2
    y = RK4(func, t, y, dt)
    t += dt
    t1list.append(t)
    y1list.append(y[0])

plt.figure(1)
plot(t1list, y1list)
plt.title('Figure 12.2')
plt.xlabel('t')
plt.ylabel('$\phi$')
plt.text(0.5, .3, '$\gamma=0.2$')
#Figure 12.4 
t=0.0
y = array([0.0 , 0.0]) 
t1list = [t]
y1list = [y[0]]

for i in range(1500):
    Y = 1.06
    y = RK4(func, t, y, dt)
    t += dt
    t1list.append(t)
    y1list.append(y[0])
    
plt.figure(2)    
plot(t1list, y1list)
plt.title('Figure 12.4')
plt.xlabel('t')
plt.ylabel('$\phi$')
plt.text(1, 10, '$\gamma=1.06$')
#Figure 12.5a 
t=0.0
y = array([0.0 , 0.0])
t2list = [t]
y2list = [y[0]]

for i in range(3000):
    Y = 1.073
    y = RK4(func, t, y, dt)
    t += dt
    t2list.append(t)
    y2list.append(y[0])
    
plt.figure(3)    
plot(t2list, y2list)
plt.title('Figure 12.5a' )
plt.xlabel('t')
plt.ylabel('$\phi$')
plt.text(5, -5, '$\gamma=1.073$')
#Figure 12.7 
t=0.0
y = array([0.0 , 0.0])
t1list = [t]
y1list = [y[0]]

for i in range(1400):
    Y = 1.077
    y = RK4(func, t, y, dt)
    t += dt
    t1list.append(t)
    y1list.append(y[0])
    
t=0.0
y = array([-1.*math.pi/2. , 0.0])
t2list = [t]
y2list = [y[0]]

for i in range(1400):
    Y = 1.077
    y = RK4(func, t, y, dt)
    t += dt
    t2list.append(t)
    y2list.append(y[0])
    
plt.figure(4)   
plot(t2list, y2list)
plot(t1list, y1list, "r--")
plt.title('Figure 12.7' )
plt.xlabel('t')
plt.ylabel('$\phi$')
plt.text(1, 10, '$\gamma=1.073$')
show()  
    
#figure 12.17
t = 0.0
y = array([-1.*math.pi/2. , 0.0])
t2list = [t]
y2list = [y[0]]
dt = .001
Yval = np.linspace(1.0600, 1.0870, 271)
MasterYlist=[]
Mastery2list=[]   
for Y in Yval:
    t2list=[]
    t = 0.0
    y = array([-1.*math.pi/2. , 0.0])     
    Ylist = []
    y2list=[]
    for i in range(600000):
        y = RK4(func, t, y, dt)
        t += dt
        t2list.append(t)
        if 500<t and t<600 and abs(t-int(t))<.001:
            y2list.append(y[0])
            Ylist.append(Y)
    Mastery2list.append(y2list)
    MasterYlist.append(Ylist)

plt.figure(4)
plot(MasterYlist, Mastery2list, '.')
plt.title('Figure 12.17')
plt.xlabel('$\gamma$')
plt.ylabel('$\phi$')
