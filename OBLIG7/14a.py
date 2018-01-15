import numpy as np
from math import exp,pi
import matplotlib.pyplot as plt

# Genererer posisjonsarray
delta_x = 0.1;
mx = 20
mn = -20
Iterations = (mx - mn)/delta_x
x = np.linspace(min,max,Iterations);


# Genererer posisjoner ved t=0
sigma = 2.0;
u = exp(-(x/(2.0*sigma))*(x/(2*sigma))); # Gaussisk form
plt.plot(x,u,'-r');

E = 1.0;
lmbda = 2*40/1.0;
l = 2*pi /lmbda ;
u = E*exp(-(x*1/(2*sigma))*2);
u_init = u ;


# Genererer div parametre og tidsderivert av utslag ved t=0
v = 0.5;
delta_t = 0.1;
faktor = (delta_t*v/delta_x)**2;
dudt = (v/(2.0*sigma*sigma))*x*u;

# Angir effektive initialbetingelser:
u_jminus1 = u - delta_t*dudt;
u_j = u;

for t in range(1,1000):
    u_jplus1(2:n-1) = ((2*(1-faktor))*u_j(2:n-1) - u_jminus1(2:n-1) + faktor*(u_j(3:n)+u_j(1:n-2)));
    # Haandtering av randproblemet, dvs setter u_j(-1) = u_j(n+1) = 0
    u_jplus1(1) = (2*(1-faktor))*u_j(1) - u_jminus1(1) + faktor*u_j(2);
    u_jplus1(n) = (2*(1-faktor))*u_j(n) - u_jminus1(n) + faktor*u_j(n-1);
    
    plt.plot(u_j);
    plt.axis([0, n+1, -0.3, 1.2])


    u_jminus1 = u_j;
    u_j = u_jplus1;


plt.plot(x , u_init,'−−r')
plt.hold("on")
plt.plot(x , u_j,, 'k')