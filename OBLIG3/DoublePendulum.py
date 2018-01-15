# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 15:27:54 2017

@author: lbnc
"""
    
def diffEq( y, t ):
    
    g = 9.81
    
    m1 = 2.
    l1 = 3.

    m2 = 2.
    l2 = 3.
    
    tdd1_h1 = -m2*l1*y[0]**2*np.sin(y[1]-y[3])*np.cos(y[1]-y[3])
    tdd1_h2 = g*m2*np.sin(y[3])*np.cos(y[1]-y[3])
    tdd1_h3 = -m2*l2*y[2]**2*np.sin(y[1]-y[3])
    tdd1_h4 = -(m1+m2)*g*np.sin(y[1])
    tdd1_h5 = l1*(m1+m2) - m2*l1*np.cos(y[1]-y[3])**2
    
    if tdd1_h5 == 0.:
        tdd1 = 0.
    else:
        tdd1 = ( tdd1_h1 + tdd1_h2 + tdd1_h3 + tdd1_h4 )/tdd1_h5
    
    tdd2_h1 = m2*l2*y[2]**2*np.sin(y[1]-y[3])*np.cos(y[1]-y[3])
    tdd2_h2 = g*(m1+m2)*np.sin(y[1])*np.cos(y[1]-y[3])
    tdd2_h3 = (m1+m2)*l1*y[0]**2*np.sin(y[1]-y[3])
    tdd2_h4 = -(m1+m2)*g*np.sin(y[3])
    tdd2_h5 = l2*(m1+m2) - m2*l2*np.cos(y[1]-y[3])**2

    if tdd2_h5 == 0.:
        tdd2 = 0.
    else:
        tdd2 = ( tdd2_h1 + tdd2_h2 + tdd2_h3 + tdd2_h4 )/tdd2_h5
    
    return np.array( [tdd1, y[0], tdd2, y[2] ] )

def RK4( y, t, dt ):
    k1 = diffEq( y, t )
    k2 = diffEq( y+k1*dt/2., t+dt/2. )
    k3 = diffEq( y+k2*dt/2., t+dt/2. )
    k4 = diffEq( y+k3*dt, t+dt )
    l = ( k1 + 2.*k2 + 2*k3 + k4 )/6.
    return( y+l*dt )

import numpy as np
import matplotlib.pyplot as plt

nT = 5000

ts = np.zeros( nT )
ys = np.zeros( [nT, 4] )

ts[0] = 0.
ys[0,:] = np.array( [0., 70./180.*np.pi, 0., 0./180.*np.pi ] )
dt = 0.05

for t in range(1,nT):
    ts[t] = ts[t-1] + dt
    ys[t,:] = RK4( ys[t-1,:], ts[t-1], dt )

# plot hastighet av pendel 1 mot hastigheten av pendel 2
plt.plot( ys[:,1], ys[:,3] )