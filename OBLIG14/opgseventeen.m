fn = '3.m4a'; %Filnavn (?l maa ligge i arbeidsmappa)
N = 2^16;

[fs, h, X] = lesm4afil(fn,N);

%Autokorrelasjon
M = N/2;
C=zeros((N-M),1);
time=zeros((N-M),1);
C = [];
time = [];
g_i_g_ij = 0;
g_i_g_i = 0;

C(1) = 1;
time(1) = 0;
for j=1:(N-M)
    for i=1:M
        g_i_g_ij = g_i_g_ij + (h(i)*h(i+j));
        g_i_g_i = g_i_g_i + (h(i)*h(i));
    end
    C(j+1) = g_i_g_ij/g_i_g_i;
    time(j+1) = j/fs;
end

figure ()
plot(time, abs(C))
title ('Autokorrelasjon')
xlabel('Tid, [s] ')
ylabel('C')
hold on
plot([0 0.01], [1/exp(1) 1/exp(1)], 'r-')
plot([0.00255 0.00255],[0 1], 'r--')
axis([0 0.01 0 1])
hold off
legend('Autokorrelasjon','1/e', '\tau_c')


%Wavelettransformasjon
f_min = 100; 
f_max = 600; 
K1 = 24;
K2 = 96;

wltransf(X,f_min,f_max,K1,N,fs)
wltransf(X,f_min,f_max,K2,N,fs)