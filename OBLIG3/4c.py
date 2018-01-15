import numpy as np
import matplotlib.pyplot as mlp

def diffEq( y, t ):
    l = 10 # fjaerkonstant i kg/s**2
    m = 100.*10**-3 # masse i kg
    w_0 = np.sqrt( l/m ) # egenfrekvens i Hz
    b = 0.04 # friksjonskoeffisient
    gamma = b/(2*m)
    w_f = np.sqrt(w_0**2 - gamma**2)  #b**2/(2*m)
    F_f = 0.1
    return( np.array([ y[1], -w_0**2*y[0]-2*gamma*y[1]+(F_f/m)*np.cos(w_f*t) ]) )

def RK4( y, t, dt ):
    k1 = diffEq( y, t )
    k2 = diffEq( y+k1*dt/2., t+dt/2. )
    k3 = diffEq( y+k2*dt/2., t+dt/2. )
    k4 = diffEq( y+k3*dt, t+dt )
    l = ( k1 + 2.*k2 + 2*k3 + k4 )/6.
    return( y+l*dt )

T = 25.     # total tid i sekund
nn = 1000    # antal tidsskritt
dt = T/nn   # tidskritt

t = np.zeros(nn)
t[0] = 0.
vec = np.zeros(( nn, 2))
#ana = np.zeros((nn,2))
vec[0,0] = 0.1      #startposisjon                                                  , analytic[0,0]
vec[0,1] = 0        #starthastighet                                                  , analytic[0,1]

for i in range( 1, nn ):    # gaa et tidskritt
    t[i] = t[i-1] + dt 
    vec[i,:] = RK4( vec[i-1,:], t[i-1], dt )
    #ana[i-1,0],ana[i-1,1] = analytic(0.5, 10, 0.1, -0.05, t[i])                 #-0.1*np.exp(-t(i)/2)*np.cos(9.9875*t[i]-0.05)
                                                                                #-0.05*np.exp(-t(i)/2)*np.cos(9.9875*t[i]-0.05)-np.exp(-t(i)/2)*np.sin(9.9875*t[i]-0.05)
mlp.plot( t, vec[:,0], 'r', t, vec[:,1], 'g' )
mlp.legend(["Utslag [m]", "Hastighet [m/s]"])
mlp.xlabel("tid[s]")
mlp.ylabel("utslag[m]/hastighet[m/s]")
mlp.show()

