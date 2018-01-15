import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlib.animation as animation
from Streng import *

# Initial conditions
m           = 0.02                  # point masses
Iterations  = 1200                  # number of iterations
N           = 200                   # number of x value (how far the string stretches)
k           = 10.0                  # spring constant
dt          = 1*np.sqrt(m/k)     # time interval

y_minus = np.zeros(N)        #y-positions in first iteration (initial condition)
y_0 = np.zeros(N)            #y-positions in second iteration (initial condition)
for i in range(1, N-1):
    y_0[i] =  np.sin((7.0*np.pi*i)/float(N-1.0))  
    y_minus[i] = y_0[i]

# Create string by sending initial conditions to Streng object    
S = streng(m, k, N, Iterations, dt, y_minus, y_0)   
S(True,0,0)                                         # Calculate movement of bound=true string



#simple animation code (Functions based on matplotlib.org example)
fig, ax = plt.subplots()
x = np.linspace(0,N-1,N)
line, = ax.plot(x, S.y_history[0])
ax.set_xlabel("punktmasse i")
ax.set_ylabel("Utslag i y retning")
ax.set_ylim([-1,1])
ax.set_xlim([0,N])
ax.set_title('Streng med sinusfunksjon som initialutslag')

def animate(l):
    line.set_ydata(S.y_history[l])  
    return line,

def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

#print and save plot     
def savePlot(filename, frame):   
    fig2, ax2 = plt.subplots()
    ax2.plot(x, S.y_history[frame])
    ax2.set_xlabel("punktmasse i")
    ax2.set_ylabel("Utslag i y retning")
    ax2.set_ylim([-1,1])
    ax2.set_xlim([0,N])
    fig2.savefig(str(filename)+'.png')

plt.rcParams['animation.ffmpeg_path'] = 'C:\\FFmpeg\\bin\\ffmpeg.exe' #path for windows where you've placed FFmpeg        
FFwriter = animation.FFMpegWriter(fps=30, extra_args=['-vcodec', 'libx264'])
ani = animation.FuncAnimation(fig, animate, np.arange(0, Iterations), init_func=init, interval=25, blit=True)   
plt.show()                                              #show string movement
for i in range(0,61,6):
    savePlot("Oppgave4_plot_frame"+str(i),i)            #store 11 images of one period
ani.save('Oppgave4_animation.mp4', writer = FFwriter)   #save mp4 animation file

      

#quick note. I had an accident where i tried to rename some variables in one file, and due 
#to how eclipse works, the variables got renamed in all files. I think the problem has been
#fixed, but there could be stray variables with the wrong name (l and k)






