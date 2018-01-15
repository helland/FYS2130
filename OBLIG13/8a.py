import numpy as np
import matplotlib.pyplot as plt

def f(c1,f1,c2,f2,t):
    return c1 * np.sin(2*np.pi*f1*t) + c2 * np.sin(2*np.pi*f2*t)

def savePlot(filename):
    plt.show()
    fig.savefig(str(filename)+'.png')               

def multiPlot(t, y, ylabel, xlabel, P, LineAppearance): 
    ax2 = fig.add_subplot(P[0],P[1],P[2])         
    ax2.set_ylabel(ylabel)    
    ax2.set_xlabel(xlabel) 
    ax2.plot(t, y, LineAppearance)  
   
f1 = 1000.0                 
f2 = 1600.0                  
N  = 8192.0                 
fs = 10000.0
c1 = 1.0
c2 = 1.7
t = np.linspace(0,N/fs,N)
f = f(c1,f1,c2,f2,t)

# choose subset to plot
plot_min,plot_max = 1000, 1250
f_plot = f[plot_min:plot_max]
t_plot = t[plot_min:plot_max]

fig = plt.figure()    
multiPlot(t_plot, f_plot, "f(t)", "t",[1,1,1],'b') 
savePlot("Oppgave8a_plot")






