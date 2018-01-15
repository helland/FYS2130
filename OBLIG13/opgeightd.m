f1 = 1000.0;                 
f2 = 1600.0;                  
N  = 8192;               
fs = 10000.0;
c1 = 1.0;
c2 = 1.7;
t = linspace(0,N/fs,N);
t1 = 0.15
t2 = 0.5
sigma1 = 0.01
sigma2 = 0.1
K = 12;

f = c1.*sin(2.*pi.*f1.*t).*exp(-((t-t1)/sigma1).^2) + c2.*sin(2.*pi.*f2.*t).*exp(-((t-t2)/sigma2).^2);
F = fft(f,N)/N;

wl = wltransf(F,800,2000,K,N,fs)


