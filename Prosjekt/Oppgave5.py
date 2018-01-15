import numpy as np
import matplotlib.pyplot as plt
from Streng import *

# Initial conditions
m           = 0.02                  #masses
Iterations  = 0                     #There is no predetermined number of iterations
N           = 200                   #number of x value (how far the string stretches)
k           = 10.0                  #spring constant
dt          = 1*np.sqrt(m/k)     #time interval

y_minus = np.zeros(N)        #y-positions in first iteration (initial condition)
y_0 = np.zeros(N)            #y-positions in second iteration (initial condition)
for i in range(0, N-1):
    y_0[i] = y_minus[i] = np.sin(7.0*np.pi*(i/(N-1.0)))    #np.sin(7.0*np.pi*(i/(N-1.0)))    # y- = y0      
     


# Create string by sending initial conditions to Streng object    
S = streng(m, k, N, Iterations, dt, y_minus, y_0)   
S(True,10,99)                                       # Calculate movement until point 99 has traveled 10 periods



# initialize Fourier & time plot values
t = np.linspace(0,len(S.y_history),len(S.y_history))
y_99 = np.zeros(len(S.y_history))
T = int(S.t/S.dt) #10 x period
print "10*T =",T,"dt =",S.t,"sekund"  
print "f =",1/S.t
for i in range(0,len(S.y_history)):
    y_99[i] = S.y_history[i][99]        #extract y_99 values

#Fourier
F = np.fft.fft(y_99,T)/T
freq = np.fft.fftfreq(T, d=S.dt)
freq = np.abs(freq[:T])  
F = (2*np.abs(F[:T]))**2  

# Function to create multiple plots in one
def multiPlot(t, y, ylabel, xlabel,y_axes,x_axes, P, LineAppearance): 
    ax2 = fig.add_subplot(P[0],P[1],P[2])         
    ax2.set_ylabel(ylabel)    
    ax2.set_xlabel(xlabel) 
    ax2.set_ylim(y_axes)
    ax2.set_xlim(x_axes) 
    ax2.plot(t, y, LineAppearance)  
    
#print and save plot     
def savePlot(filename):
    plt.show()
    fig.savefig(str(filename)+'.png')               
   
fig = plt.figure()     #Shared figure for plots
multiPlot(t, y_99, "y_99(t)", "tid [dt]",[-1,1],[0,len(S.y_history)],[2,1,1],'r') #y(t)
multiPlot(freq, F, "Koeffisient", "Frekvens [Hz]",[-0.1,1.1],[0,1],[2,1,2],'b*')  #fft
savePlot("Oppgave5_plot")

