function [fs,h,X] = lesm4afil(filename,N)

%Digitaliserer lyden
[f ,fs] = audioread(filename, [N 2*N-1]) ;
%sound(f,fs); %Spiller av lyden igjen dersom man vil

h = f (:,1) ; %Henter ut ett monosignal fra stereosignalet f
X = (1.0/N)*fft(h); %Fast Fourier Transform av lydsignalet

%plot
figure ()
freq = (fs/2)*linspace(0,1,N/2); %frequency
plot(freq,2*abs(X(1:N/2)))
xlabel('Frekvens [Hz]')
ylabel(' |FFT|^2 Koeff.')
hold on
plot(116.54,2*max(abs(X)),'ro')
axis([100 750 0 0.125])
legend('FFT','B_2b')
hold off


