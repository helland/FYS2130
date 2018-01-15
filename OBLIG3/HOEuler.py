import numpy as np
import matplotlib.pyplot as mlp

# konstanter
l = 1. # fjaerkonstant i kg/s**2
m = 1. # masse i kg

# egenfrekvens i Hz
omega_0 = np.sqrt( l/m )

# tidskritt i s
delta_t = 0.01

# antal tidsskritt
nn = 5000

# array for tid
t = np.empty( nn )
# array for utslaget
x = np.empty( nn )
# array for hastighet
v = np.empty( nn )

# initialbetingelser
t[0] = 0.
x[0] = 0. # initiale utslaget er 0
v[0] = 1. # initiale hastigheten er 1 m/s

for i in range( 1, nn ):

    # gaa et tidskritt
    t[i] = t[i-1] + delta_t

    # hastighet
    v[i] = v[i-1] - omega_0**2*x[i-1]*delta_t
    # posisjon
    x[i] = x[i-1] + v[i-1]*delta_t

# beregner potensielle energi
e_p = 0.5*l*x**2

# beregner kinetisk energi
e_k = 0.5*m*v**2

mlp.plot( t, x, 'r', t, v, 'g' )
mlp.xlabel("tid")
mlp.ylabel("utslag/hastighet")
mlp.show()