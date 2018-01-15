import numpy as np
import matplotlib.pyplot as mlp

def diffEq( y, t ):
    # konstanter
    l = 1. # fjaerkonstant i kg/s**2
    m = 1. # masse i kg
    # egenfrekvens i Hz
    omega_0 = np.sqrt( l/m )
    return( np.array([ y[1], -omega_0**2*y[0] ]) )

def RK4( y, t, dt ):
    k1 = diffEq( y, t )
    k2 = diffEq( y+k1*dt/2., t+dt/2. )
    k3 = diffEq( y+k2*dt/2., t+dt/2. )
    k4 = diffEq( y+k3*dt, t+dt )
    l = ( k1 + 2.*k2 + 2*k3 + k4 )/6.
    return( y+l*dt )

# tidskritt
dt = 0.2
# antal tidsskritt
nn = 100

t = np.empty( nn )
t[0] = 0.
vec = np.empty( [ nn, 2] )
vec[0,0] = 0.
vec[0,1] = 1.

for i in range( 1, nn ):

    # gaa et tidskritt
    t[i] = t[i-1] + dt
    vec[i,:] = RK4( vec[i-1,:], t[i-1], dt )

mlp.plot( t, vec[:,0], 'r', t, vec[:,1], 'g' )
mlp.xlabel("tid")
mlp.ylabel("utslag/hastighet")
mlp.show()