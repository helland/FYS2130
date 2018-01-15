import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlib.animation as animation
from Streng import *

# Initial conditions
m           = 0.02                  #masses
Iterations  = 1200                  #number of iterations
N           = 200                   #number of x value (how far the string stretches)
k           = 10.0                  #spring constant
dt          = 1*np.sqrt(m/k)        #time interval

y_minus = np.zeros(N)        #y-positions in first iteration (initial condition)
y_0 = np.zeros(N)            #y-positions in second iteration (initial condition)
for i in range(0, N-1):      #fill initial iterations for desired wave function
    if (1 <= i and i <= 30):
        y_0[i]      = i/30.0
        y_minus[i]  = y_0[i-1]  #place y-[i] in the previous position of y0[i] 
    elif (31 <= i and i <= 61):
        y_0[i]      = (61-i)/31.0
        y_minus[i]  = y_0[i-1]
    else:
        y_0[i]      = 0  
        y_0[i-1]    = y_0[i]



# Create string by sending initial conditions to Streng object    
S = streng(m, k, N, Iterations, dt, y_0, y_minus)   
S(True,0,0)                                         # Calculate movement of bound=true string



#simple animation code (Functions based on matplotlib.org example)
fig, ax = plt.subplots()
x = np.linspace(0,N-1,N)
line, = ax.plot(x, S.y_history[0])
ax.set_xlabel("Punktmasse i")
ax.set_ylabel("Y Posisjon")
ax.set_ylim([-1,1])
ax.set_xlim([0,N])
ax.set_title('Trekantet initialutslag med bevegelse mot hoyre')

def animate(l):
    line.set_ydata(S.y_history[l])  
    return line,

def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

plt.rcParams['animation.ffmpeg_path'] = 'C:\\FFmpeg\\bin\\ffmpeg.exe' #path for windows where you've placed FFmpeg
FFwriter = animation.FFMpegWriter(fps=30, extra_args=['-vcodec', 'libx264'])
ani = animation.FuncAnimation(fig, animate, np.arange(0, Iterations), init_func=init, interval=10, blit=True)

fig2, ax2 = plt.subplots()
for i in range(0,300,50):
    ax2.plot(x, S.y_history[i])
    ax2.set_xlabel("punktmasse i")
    ax2.set_ylabel("Utslag i y retning")
    ax2.set_ylim([-1,1])
    ax2.set_xlim([0,N])
fig2.savefig("Oppgave7_plot2_frame"+'.png')


plt.show()
ani.save('Oppgave8_animation.mp4', writer = FFwriter) 


