import numpy as np
import matplotlib.pyplot as mlp

def diffEq(b, y, t):
    l = 10 # fjaerkonstant i kg/s**2
    m = 100.*10**-3 # masse i kg
    w_0 = np.sqrt( l/m ) # egenfrekvens i Hz
    gamma = b/(2*m)
    return( np.array([ y[1], -w_0**2*y[0]-2*gamma*y[1] ]) )

def RK4(b, y, t, dt):
    k1 = diffEq(b, y, t )
    k2 = diffEq(b, y+k1*dt/2., t+dt/2. )
    k3 = diffEq(b, y+k2*dt/2., t+dt/2. )
    k4 = diffEq(b, y+k3*dt, t+dt )
    l = ( k1 + 2.*k2 + 2*k3 + k4 )/6.
    return( y+l*dt )

T = 10.     # total tid i sekund
nn = 1000    # antal tidsskritt
dt = T/nn   # tidskritt

t = np.zeros(nn)
t[0] = 0.
vec = np.zeros(( nn, 2)) 
vec[0,0] = 0.1    #startposisjon                                                  , analytic[0,0]
vec[0,1] = 0.0     #starthastighet                                                  , analytic[0,1]

bb = [0.1, 20*0.1,40*0.1]
for i in range(0,len(bb)):
    b = bb[i]
    for i in range( 1, nn ):    # gaa et tidskritt
        t[i] = t[i-1] + dt 
        vec[i,:] = RK4(b, vec[i-1,:], t[i-1], dt  )
                                                                          
    mlp.plot( t, vec[:,0] ) 
    mlp.hold("on")
mlp.legend(["Underkritisk demping [m]", "Kritisk demping [m]", "overkritisk demping [m]"])
mlp.xlabel("tid[s]")
mlp.ylabel("utslag[m]")
mlp.show()



#vec2 = np.zeros((nn,2)) #l  , vec2[0,0], vec3[0,0]
#vec3 = np.zeros((nn,2)) #ok  ,vec2[0,1],vec3[0,1]
#'r', t, vec2[:,0], 'g',t, vec3[:,0], 'b--' 
        #vec2[i,:] = RK4(b, vec2[i-1,:], t[i-1], dt  )
        #vec3[i,:] = RK4(b, vec3[i-1,:], t[i-1], dt )