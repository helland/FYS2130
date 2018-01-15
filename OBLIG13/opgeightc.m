f1 = 1000.0;                 
f2 = 1600.0;                  
N  = 8192;               
fs = 10000.0;
c1 = 1.0;
c2 = 1.7;
t = linspace(0,N/fs,N);
K = 1000
f = c1.*sin(2.*pi.*f1.*t) + c2.*sin(2.*pi.*f2.*t);
F = fft(f,N)/N;

wl = wltransf(F,800,2000,K,N,fs);







