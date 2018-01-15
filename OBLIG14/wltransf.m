function [msg] = wltransf(FTsignal,fmin,fmax,K,N,fs)


% Beregner # analysefrekvenser, skriver til skjerm, klargjor frekvensene
M = floor(log(fmax/fmin) / log(1+(1/(8*K)))) + 1;
AntallFrekvenserIAnalyse = M
ftrinn = (fmax/fmin)^(1/(M-1));
f_analyse = fmin;
T = N/fs; % Total tid lydutsnittet tar (i sek)
t = linspace(0,T*(N-1)/N,N);
f = linspace(0,fs*(N-1)/N, N);

% Allokerer plass til waveletdiagrammet og array for lagring av frekvenser
WLdiagram = zeros(M,N);
fbrukt = zeros(1,M);

%  kke over alle frekvenser som inngaar i analysen
for jj = 1:M
    faktor = (K/f_analyse)*(K/f_analyse);
    FTwl = exp(-faktor*(f-f_analyse).*(f-f_analyse));
    FTwl = FTwl - exp(-K*K)*exp(-faktor*(f.*f)); % Lite korreksjonsledd
    FTwl = 2.0*FTwl; % Faktor (ulike valg!)
    % Beregner s  en hel linje i waveletdiagrammet i  n jafs!
    %WLdiagram(jj,:) = abs(ifft(FTwl.*transpose(FTsignal)));% Ett alternativ
    WLdiagram(jj,:) = sqrt(abs(ifft(FTwl.*transpose(FTsignal)))); % Ett annet
    % Bruker den siste varianten for aa f  svake partier bedre synlig
    fbrukt(jj) = f_analyse; % Lagrer frekvensene som faktisk er brukt
    f_analyse = f_analyse*ftrinn; % Beregner neste frekvens
end;

% Reduserer filstorrelse ved aa fjerne mye av overfldig informasjon i tid.
P = floor((K*fs)/(24 * fmax)); % Tallet 24 kan endres ved behov
TarBareMedHvertXITid = P % Skriver til skjerm (monitorering)
NP = floor(N/P);
AntallPktITid = NP % Skriver til skjerm (monitorering)
WLdiagram2 = zeros(N,NP);
tP = zeros(1,NP);
for jj = 1:M
    for ii = 1:NP
        WLdiagram2(jj,ii) = WLdiagram(jj,ii*P);
        tP(ii) = t(ii*P);
    end;
end;

% Foreta en markering i plottet for aa vise omraader med randproblemer
maxverdi = max(WLdiagram2);
mxv = max(maxverdi);

for jj = 1:M
    m = floor(K*fs/(P*pi*fbrukt(jj)));
    WLdiagram2(jj,m) = mxv/2;
    WLdiagram2(jj,NP-m) = mxv/2;
end;
% Plotter waveletdiagrammet
figure;
imagesc(tP,log10(fbrukt),WLdiagram2);
set(gca,'YDir','normal');
xlabel('Tid (sek)');
ylabel('Log10(frekvens i Hz)');
%title('Wavelet Power Spektrum'); 
title('Sqrt(Wavelet Power Spektrum)'); % denne naar sqrt blir brukt
colorbar('location','southoutside');

msg = 'Done!';