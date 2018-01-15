import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlib.animation as animation
from Streng import *

# Initial conditions
m           = 0.02                  #masses
Iterations  = 2500                  #number of iterations
N           = 200                   #number of x value (how far the string stretches)
k           = 10.0                  #spring constant
dt          = 0.99*np.sqrt(m/k)        #time interval

y_minus = np.zeros(N)        #y-positions in first iteration (initial condition)
y_0 = np.zeros(N)            #y-positions in second iteration (initial condition)
for i in range(0, N-1):      #fill initial iterations for desired wave function
    if (70 <= i and i <= 99):
        y_minus[i]  = (i-69.0)/30.0
        y_0[i]      = (i-69.0)/30.0
    elif (100 <= i and i <= 128):
        y_minus[i]  = (129.0-i)/30.0
        y_0[i]      = (129.0-i)/30.0
    else:
        y_minus[i]  = 0
        y_0[i]      = 0    



# Create string by sending initial conditions to Streng object        
S = streng(m, k, N, Iterations, dt, y_minus, y_0)   
S(True,0,0)                                         # Calculate movement of bound=true string



#simple animation code (Functions based on matplotlib.org example)
fig, ax = plt.subplots()
x = np.linspace(0,N-1,N)
line, = ax.plot(x, S.y_history[0])
ax.set_xlabel("punktmasse i")
ax.set_ylabel("y posisjon")
ax.set_ylim([-1,1])
ax.set_xlim([0,N])
ax.set_title('Sentrert trekantet initialutslag ')

def animate(l):
    line.set_ydata(S.y_history[l])  
    return line,

def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

    

plt.rcParams['animation.ffmpeg_path'] = 'C:\\FFmpeg\\bin\\ffmpeg.exe' #path for windows where you've placed FFmpeg
FFwriter = animation.FFMpegWriter(fps=30, extra_args=['-vcodec', 'libx264'])
ani = animation.FuncAnimation(fig, animate, np.arange(0, Iterations), init_func=init, interval=10, blit=True) #increase interval to slow down animation
fig2, ax2 = plt.subplots()
for i in range(0,300,50):
    ax2.plot(x, S.y_history[i])
    ax2.set_xlabel("punktmasse i")
    ax2.set_ylabel("Utslag i y retning")
    ax2.set_ylim([-1,1])
    ax2.set_xlim([0,N])
fig2.savefig("Oppgave7_plot2_frame"+'.png')

plt.show()
ani.save('Oppgave7_animation.mp4', writer = FFwriter) 









