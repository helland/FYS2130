
# 
import matplotlib.pyplot as plt
import numpy as np

# Initialize variables
N = 200
y_prev = np.zeros(N)
y_now = np.zeros(N)
y_next = np.zeros(N)

x = np.linspace(0, N-1, N)

# Time steps
n = 1200

# Create an array of masses [kg]
m = np.zeros(N) + 0.02
m[0] = m[N-1] = 1000

# Create an array of l
l = np.zeros(N) + 10.0  # [kg/s**2]

# Find dt based on calculations from problem 3: dt = sqrt(m/l)
dt = 0.9*np.sqrt(m[1]/l[1])  # [s]


# Set initial wave
for i in range(0,N-1):
    y_prev[i] = y_now[i] = np.sin((7*np.pi*i)/float(N-1))

# 
for i in range(0,n):
    # Handle boundaries for i=0 and i=(N-1)
    i = 0
    y_next[i] = 2*y_now[i]-y_prev[i] + (l[i]*(y_now[i+1]-y_now[i]))*((dt**2)/m[i])

    i = N-1
    y_next[i] = 2*y_now[i]-y_prev[i] + (l[i-1]*(y_now[i-1]-y_now[i]))*((dt**2)/m[i])

    # Calculate y_next for 1<=i<=(N-2)
    for i in range(1,N-2):
        y_next[i] = 2*y_now[i] - y_prev[i] + (l[i-1]*y_now[i-1] + l[i]*y_now[i+1] - l[i-1]*y_now[i] - l[i]*y_now[i])*((dt**2)/m[i])

    # plot frame
    if i==0 or i==100:
        plt.plot(x, y_now)

    #
    for i in range(N-1): 
        y_prev[i] = y_now[i]
        y_now[i] = y_next[i]

# Plot
#plt.legend(['t=200','t=400'],loc='upper right')
plt.xlabel('[x]')
plt.ylabel('[y]')
plt.show()



