import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlib.animation as animation
from Streng import *
from sympy.physics.quantum.tests.test_sho1d import a_rep

# Initial conditions
N           = 400                   #number of x value (how far the string stretches)
m           = np.zeros(N)           #masses
Iterations  = 2400                  #number of iterations
k           = 10.0                  #spring constant
dt          = 1*np.sqrt(0.02/k)     #time interval with lowest mass value

y_minus = np.zeros(N)        #y-positions in first iteration (initial condition)
y_0 = np.zeros(N)            #y-positions in second iteration (initial condition)

for i in range(0, N-1):      #fill initial iterations for desired wave function
    if (1 <= i and i <= 30):
        y_0[i]      = i/30.0
        y_minus[i]  = y_0[i-1]
    elif (31 <= i and i <= 61):
        y_0[i]      = (61-i)/31.0
        y_minus[i]  = y_0[i-1]
    else:
        y_0[i]      = 0  
        y_0[i-1]    = y_0[i]

for i in range(0, N):        #add two different masses to the first and last N/2 elements
    if i < N/2:
        m[i] = 0.02          #low mass m for the first 200
    else:
        m[i] = 0.06          #high mass 3*m for the next 200



# Create string by sending initial conditions to Streng object     
S = streng(m, k, N, Iterations, dt, y_0, y_minus)   
S(True,0,0)                                         # Calculate movement of bound=true string


A_r = 0 #reflected amplitude
A_t = 0 #transmitted amplitude
#finn A_r og A_t
for j in range(0, len(S.y_history[350])-1):
    if S.y_history[350][j] <= A_r:
        A_r = S.y_history[350][j]
    if S.y_history[350][j] >= A_t:
        A_t = S.y_history[350][j]


print "Reflektert A_r:",A_r
print "transmitert A_t:",A_t                    #
print "A_r + A_t = ",np.abs(A_r) +np.abs(A_t)   #total after 
print "A_r / A_t = ",np.abs(A_r)/np.abs(A_t)    #ratio

#simple animation code (Functions based on matplotlib.org example)
fig, ax = plt.subplots()
x = np.linspace(0,N-1,N)
line, = ax.plot(x, S.y_history[0])
ax.set_xlabel("punktmasse i")
ax.set_ylabel("y posisjon")
ax.set_ylim([-1,1])
ax.set_xlim([0,N])
ax.set_title('Strengbevegelse hvor punktmassene ikke er like')

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
for i in range(0,800,125):
    ax2.plot(x, S.y_history[i])
    ax2.set_xlabel("punktmasse i")
    ax2.set_ylabel("Utslag i y retning")
    ax2.set_ylim([-1,1])
    ax2.set_xlim([0,N])
fig2.savefig("Oppgave9_plot"+'.png')



plt.show()
ani.save('Oppgave9_animation.mp4', writer = FFwriter) 

