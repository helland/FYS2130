import numpy as np
import matplotlib.pyplot as mlp

def diffEq( y, t ):
    l = 10 # fjaerkonstant i kg/s**2
    m = 100.*10**-3 # masse i kg
    w_0 = np.sqrt( l/m ) # egenfrekvens i Hz
    b = 0.04 # friksjonskoeffisient
    gamma = b/(2*m)
    #w_f = np.sqrt(w_0**2 - gamma**2)  #b**2/(2*m)
    F_f = 0.1
    return( np.array([ y[1], -w_0**2*y[0]-2*gamma*y[1]+(F_f/m)*np.cos(w_f*t)]) )

def RK4( y, t, dt ):
    k1 = diffEq( y, t )
    k2 = diffEq( y+k1*dt/2., t+dt/2. )
    k3 = diffEq( y+k2*dt/2., t+dt/2. )
    k4 = diffEq( y+k3*dt, t+dt )
    l = ( k1 + 2.*k2 + 2*k3 + k4 )/6.
    return( y+l*dt )

T = 50.     # total tid i sekund
nn = 1000    # antal tidsskritt
dt = T/nn   # tidskritt
t = np.zeros(nn)
t[0] = 0.
vec = np.zeros(( nn, 2))
vec[0,0] = 0.1      #startposisjon                                                  , analytic[0,0]
vec[0,1] = 0        #starthastighet                                                  , analytic[0,1]
wf_vec = np.linspace(5, 15, nn/10)
E_max = np.zeros(nn/10)

for i in range(0,nn/10):
    w_f = wf_vec[i]
    
    for i in range( 1, nn ):    # gaa et tidskritt
        t[i] = t[i-1] + dt 
        vec[i,:] = RK4( vec[i-1,:], t[i-1], dt )
    amp = vec[800:,0]
    max_amp = np.amax(amp) 
    E_max[i] = (1.0/2.0)*10*(max_amp)**2 

freq = wf_vec*(1.0/(2.0*np.pi))
line = np.linspace(0,0.35,10)
line2 = np.linspace(0,2.5,10)
energy = np.ones(10)*np.amax(E_max)
energy2 = np.ones(10)*(np.amax(E_max)*0.5)
f_0_line = np.ones(10)*(10.0/(2*np.pi))

mlp.plot( freq, E_max, "b", line2, energy, "g--", line2,energy2,"m--", f_0_line, line, "b--" )
mlp.legend( [ "E(f)" , "E_max", "E_max /2" , "f_0"] )
mlp.xlabel("Frekvens  [Hz]")
mlp.ylabel("Energi [J]")
mlp.show()

