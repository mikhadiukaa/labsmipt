import turtle as t
import numpy as np
import matplotlib.pyplot as plt
dt = 0.0001;
t.fin=100
dot_amount = t.fin/dt;
dot_amount = int(dot_amount);
x=np.zeros(dot_amount);
y=np.zeros(dot_amount);
vy0=50
vx0=500
disscoeff = 0.90
vy = np.zeros(dot_amount);
vy[0] = vy0;
g=9.8
for(i) in range (dot_amount -1):
    vy[i+1] = vy[i] - g*dt-g*vy
    x[i+1] = x[i] + vx0*dt
    y[i+1] = vy[i]*dt + y[i]
    if(y[i+1] <= 0):
        vy[i+1] = -disscoeff*vy[i];
plt.plot(x, y)
plt.show()



