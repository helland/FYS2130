import numpy as np
import matplotlib.pyplot as plt

def f(c1,f1,c2,f2,t):
    return c1 * np.sin(2*np.pi*f1*t) + c2 * np.sin(2*np.pi*f2*t)

# Function to create multiple plots in one
def multiPlot(t, y, ylabel, xlabel, P, LineAppearance): 
    ax2 = fig.add_subplot(P[0],P[1],P[2])         
    ax2.set_ylabel(ylabel)    
    ax2.set_xlabel(xlabel) 
    ax2.plot(t, y, LineAppearance)  
    
#print and save plot     
def savePlot(filename):
    plt.show()
    fig.savefig(str(filename)+'.png')               
   
f1 = 1000.0                 
f2 = 1600.0                  
N  = 8192               
fs = 10000.0
c1 = 1.0
c2 = 1.7
t = np.linspace(0,N/fs,N)
f = f(c1,f1,c2,f2,t)
dt = N/fs

# choose subset to plot
plot_min,plot_max = 1000, 1500
f_plot = f[plot_min:plot_max]
t_plot = t[plot_min:plot_max]

#Fourier
F = np.fft.fft(f,N)/N #
freq = np.fft.fftfreq(N, d=dt)*N
freq = np.abs(freq[:N])  
F = np.sqrt((2*np.abs(F[:N]))**2)

fig = plt.figure()     
multiPlot(t_plot, f_plot, "f(t)", "t",[2,1,1],'r') 
multiPlot(freq, F, "Koeffisient", "Frekvens [Hz]",[2,1,2],'b-') 
savePlot("Oppgave8b_plot")
