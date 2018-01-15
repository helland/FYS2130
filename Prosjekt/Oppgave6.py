import numpy as np
from math import pi,sin,sqrt
import matplotlib.pyplot as plt
from Streng import *

# Initial conditions
m           = 0.02                  #masses
Iterations  = 4200                  #number of iterations
N           = 200                   #number of x value (how far the string stretches)
k           = 10.0                  #spring constant
dt          = 0.01*sqrt(m/k)         #time interval

y_minus = np.zeros(N)        #y-positions in first iteration (initial condition)
y_0 = np.zeros(N)            #y-positions in second iteration (initial condition)
for i in range(0, N-1):
    y_0[i] = y_minus[i] = sin(7.0*pi*(i/(N-1.0)))  # y- = y0



# Create string by sending initial conditions to Streng object    
S = streng(m, k, N, Iterations, dt, y_minus, y_0)   
S(True,0,0)                                         # Calculate movement of bound=true string

#Find energies
E, E2 = np.zeros((Iterations-1, N)),np.zeros(Iterations-1)
E_k, E_k2 = np.zeros((Iterations-1, N)),np.zeros(Iterations-1)
E_p, E_p2 = np.zeros((Iterations-1, N)),np.zeros(Iterations-1)
E_average = 0 
  
for l in range (0,Iterations-1):    # for every iteration
    for i in range(0, N-1):         # in every point along the string
        E_k[l][i]  = 0.5*m*(float(S.y_history[l+1][i]-S.y_history[l][i])/dt)**2 #store kinetic energy in point i at time l
        E_p[l][i]  = 0.5*k*(S.y_history[l][i+1]-S.y_history[l][i])**2           #store potential energy in point i at time l
        E[l][i]  = E_k[l][i] + E_p[l][i]                                        #store total energy in point i at time l
     
    E_k2[l] = sum(E_k[l])           # Total kinetic energy in all point-masses in this iteration  
    E_p2[l] = sum(E_p[l])           # Total potential energy in all springs in this iteration  
    E2[l] = E_k2[l] + E_p2[l]       # stotal energy of the system this iteration 
    E_average = E_average + E2[l]   # add up all total energies
E_average = E_average/Iterations    # find average energy of every point in time 


# plot kinetic, potential and total energy over time
t = np.linspace(0,(Iterations)*dt,Iterations-1)   #time intervals for plot
plt.xlabel("Tid [s]")
plt.ylabel("Energi [J]")
plt.plot(t,E_k2,'r-',t,E_p2,'b',t,E2,'g--')
plt.legend(["Kinetisk Energi", "Potentiell Energi", "Total Energi"])
plt.show()

# plot deviation from the average total energy over time
average = np.linspace(E_average,E_average,Iterations-1)
Initial_Energy = np.linspace(E2[0],E2[0],Iterations-1)
plt.xlabel("Tid [s]")
plt.ylabel("Energi [J]")
plt.plot(t,Initial_Energy,'g--',t,E2,'b--') #t,average,'r-',
plt.legend(["Total energi ved t=0", "Total Energi"]) #"gjennomsnittlig Energi", 
plt.show()
   
    
    
    
    
    
    
    
    
    