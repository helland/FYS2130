import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from Streng import *

def dydt2(y_minus,y_zero,y_pluss, dt):
    return (y_pluss - 2*y_zero + y_pluss)/dt**2


def force(y_minus,y_zero,y_pluss, dt, m):
    return dydt2(y_minus,y_zero,y_pluss, dt)*m




m       = 1         #masses
t_max   = 10        #total time measured
Iterations       = 5      #number of iterations
dt      = t_max/Iterations   #time interval
N   = 10        #highest x value (how far the string stretches)
dx      = 1      #space between point masses
mu      = m/dx      #mass density

#y_minus = np.zeros(N/dx)    #y-positions in previous iteration
y_0 = np.zeros(N/dx)        #y-positions in current iteration
y_0[0] = 1
#y_pluss = np.zeros(N/dx)    #y-positions in next iteration

S = streng(m, l, N, dx, Iterations, t_max, y_0)



Y0 = np.array([0,10])       # initial conditions
mu = 1.5
rho = 1.2
omega = 1
def dY_dx(Y, t=0):
    """ Return the gradient of y1 and y2"""
    return np.array([Y[1] / mu, - (omega ** 2) * rho * Y[0]])

from scipy import integrate

Y = integrate.odeint(dY_dx, Y0, x)

y1, y2 = Y.T


# initialisation function: plot the background of each frame
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    time_text.set_text('')
    return line1, line2, time_text

# animation function: this is called sequentially
def animate(i):
    t = np.arange(0.0,40,dt) + i*dt
    Y = integrate.odeint(dY_dx,Y0,t)
    y1,y2 = Y.T

    line1.set_data(x, y1)
    line2.set_data(x, y2)

    time_text.set_text(time_template%t)
    return line1, line2, time_text
# call the animator. blit=True means only re-draw the parts that have changed
ani = animation.FuncAnimation(fig, animate, np.arange(1, len(Y)), interval=25, blit=True, init_func=init)

#ani.save('waveEquation.mp4', fps=15)
plt.show()









'''
def upperPlot(t, y, ylabel, xlabel,y_axes,x_axes): 
    ax1 = fig.add_subplot(2,1,1)                      
    ax1.set_ylabel(ylabel) 
    ax1.set_xlabel(xlabel)
    ax1.set_ylim(y_axes)
    ax1.set_xlim(x_axes) 
    ax1.plot(t, y,'r')
     
def lowerPlot(t, y, ylabel, xlabel,y_axes,x_axes): 
    ax2 = fig.add_subplot(2,1,2)         
    ax2.set_ylabel(ylabel)    
    ax2.set_xlabel(xlabel) 
    ax2.set_ylim(y_axes)
    ax2.set_xlim(x_axes) 
    ax2.plot(t, y,'b*')         

#upperPlot(t, y_99, "y_99(t)", "tid [dt]",[-1,1],[0,len(S.y_history)]) #y(t)
#lowerPlot(freq, F, "Koeffisient", "Frekvens [Hz]",[-0.1,1.1],[0,1])             #fft

# set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(0,15), ylim=(-10,10))
ax.grid()

line1, = ax.plot([], [], 'o', ms=2)
line2, = ax.plot([], [], '-', lw=2)
time_template = 'time = %.lfs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

# initialisation function: plot the background of each frame
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    time_text.set_text('')
    return line1, line2, time_text

# animation function: this is called sequentially
def animate(i):
    t = np.arange(0.0,t_max,dt) + i*dt
    Y = integrate.odeint(dY_dx,Y0,t)
    y1,y2 = Y.T

    line1.set_data(x, y1)
    line2.set_data(x, y2)

    time_text.set_text(time_template%t)
    return line1, line2, time_text
# call the animator. blit=True means only re-draw the parts that have changed
ani = animation.FuncAnimation(fig, animate, np.arange(1, len(Y)), interval=25, blit=True, init_func=init)

#ani.save('waveEquation.mp4', fps=15)
plt.show()
'''






# Initial conditions
m = 0.02 # point masses
Iterations = 1200 # number of iterations
N = 200 # number of x value (how far the string stretches)
k = 10.0 # spring constant
dt = 1 * np.sqrt(m/k) # time interval
y minus = np.zeros(N) #y−positions in ﬁrst iteration (initial condition)
y 0 = np.zeros(N) #y−positions in second iteration (initial condition)
for i in range(1, N−1):
y 0[i] = np.sin((7.0 * np.pi * i)/ﬂoat(N−1.0))
y minus[i] = np.sin((7.0 * np.pi * i)/ﬂoat(N−1.0)) − (dt * (7.0 * np.pi/ﬂoat(N−1.0)) * np.cos((7.0 * np.pi * i)/ﬂoat(N−1.0)))
# = y 0[i]
# Create string by sending initial conditions to Streng object
S = streng(m, k, N, Iterations, dt, y minus, y 0)
S(True,0,0) # Calculate movement of bound=true string
#simple animation code (Functions based on matplotlib.org example)
ﬁg, ax = plt.subplots()
x = np.linspace(0,N−1,N)
line, = ax.plot(x, S.y history[0])
ax.set xlabel(”punktmasse i”)
ax.set ylabel(”Utslag i y retning”)
ax.set ylim([−1,1])
ax.set xlim([0,N])
ax.set title(’Streng med sinusfunksjon som initialutslag’)
def animate(l):
line.set ydata(S.y history[l])
return line,
def init():
line.set ydata(np.ma.array(x, mask=True))
return line,
#print and save plot
def savePlot(ﬁlename, frame):
ﬁg2, ax2 = plt.subplots()
ax2.plot(x, S.y history[frame])
ax2.set xlabel(”punktmasse i”)
ax2.set ylabel(”Utslag i y retning”)
ax2.set ylim([−1,1])
ax2.set xlim([0,N])
ﬁg2.saveﬁg(str(ﬁlename)+’.png’)
plt.rcParams[’animation.ﬀmpeg path’] = ’C:\\FFmpeg\\bin\\ﬀmpeg.exe’ #path for windows where you’ve placed
FFmpeg
FFwriter = animation.FFMpegWriter(fps=30, extra args=[’−vcodec’, ’libx264’])
ani = animation.FuncAnimation(ﬁg, animate, np.arange(0, Iterations), init func=init, interval=25, blit=True)
plt.show() #show string movement
for i in range(0,61,6):
savePlot(”Oppgave4 plot frame”+str(i),i) #store 11 images of one period
ani.save(’Oppgave4 animation.mp4’, writer = FFwriter) #save mp4 animation ﬁle