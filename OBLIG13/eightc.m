% Hovedprogram som leser en wav-fil, plotter tidbildet
% og frekvensbildet, og dernest den wavelettransformerte.
% Leser en wavfil
function WLavWAV
  c = 'gjok.wav';
  nstart = 31000;
  N = 1024*32;
  [fs,h] = leswavfil(c,nstart,N);
  % Fouriertransformerer
  [FTsignal] = fftogplot(h,N,fs);
  % Wavelet-analyse
  fmin = 400.0; % Bestemmes ut fra FT og skjønn
  fmax = 800.0; % ds
  K = 32; % Maa optimaliseres for hvert signal
  [msg] = wltransf(FTsignal,fmin,fmax,K,N,fs);

  
  % Denne funksjonen leser en wav-fil ned filnavn c.
  % Vi starter lesingen nstart punkter etter filstarten,
  % og det leses N datapunkter fra filen.
  % Lyden spilles, og signalet plottes.
  % Funksjonen returnerer samplingsfrekvensen og
  % den ene kanalen av stereosignalet i wav-filen.
  % Denne versjonen er fra 20. april 2016 
function [fs,h] = leswavfil(c,nstart,N)

  nslutt = nstart+N-1;
  [y, fs] = audioread(c, [nstart nslutt]); % Les array y(N,2) fra fil
  % ’fs’ er vanligvis 44100 (samplingsfrekvens ved CD kvalitet)
  h = zeros(N,1); % Plukker ut bare én kanal fra stereosignalet lest
  h = y(:,1);
  sound(h,fs); % Spiller av utsnittet som er brukt
  T = N/fs; % Total tid lydutsnittet tar (i sek)
  t = linspace(0,T*(N-1)/N,N);
  plot(t,h,'-k');
  title('Wav-filens signal');
  xlabel('Tid (sek)');
  ylabel('Signal (rel enhet)');


end

% Funksjon som foretar en fft av et signal h med N punkter.
% Samplingsfrekvensen er fs. Den fouriertransformerte
% plottes (absuluttverdien), mens det komplekse
% fouriertransformerte signalet returneres til den kallende funksjon.
% Versjon 20.4.2016
% Beregner først FFT av tidsstrengen h 
function [FTsignal] = fftogplot(h,N,fs)

  FTsignal = fft(h);
  % Plotter frekvensspekteret (absoluttverdier only)
  f = linspace(0,fs*(N-1)/N, N);
  nmax = floor(N/2); % Plotter bare opp til halve samplingsfrekv.
  figure;
  plot(f(1:nmax),abs(FTsignal(1:nmax)));
  xlabel('Frekvens (Hz)');
  ylabel('Relativ intensitet');
  title('Frekvensspektrum av signal');


end

% Funksjonen foretar ALT som er involvert ved beregning
% inklusiv optimalisering av antall frekvenser som skal beregnes og antall
% punkter i tidsbeskrivelsen som skal benyttes i endelig plot.
% Som input har vi FT av signalet vi skal analysere, og
% min og max frekvens som skal inngå i wl-analysen.
% Vi kan velge mellom to ulike skaleringer av "intensitet".
% Til slutt plottes waveletdiagrammet.
% Versjon 20.4.2016
%BEREGNER DEN WAVELETTRANSFORMERTE OG PLOTTER RESULTATET
function [msg] = wltransf(FTsignal,fmin,fmax,K,N,fs)

  % Beregner # analysefrekvenser, skriver til skjerm, klargjør frekvensene
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
  % Løkke over alle frekvenser som inngår i analysen
  for jj = 1:M
    faktor = (K/f_analyse)*(K/f_analyse);
    FTwl = exp(-faktor*(f-f_analyse).*(f-f_analyse));
    FTwl = FTwl - exp(-K*K)*exp(-faktor*(f.*f)); % Lite korreksjonsledd
    FTwl = 2.0*FTwl; % Faktor (ulike valg!)
    % Beregner så en hel linje i waveletdiagrammet i én jafs!
    %WLdiagram(jj,:) = abs(ifft(FTwl.*transpose(FTsignal)));% Ett alternativ
    WLdiagram(jj,:) = sqrt(abs(ifft(FTwl.*transpose(FTsignal)))); % Ett annet
    % Bruker den siste varianten for å få svake partier bedre synlig
    fbrukt(jj) = f_analyse; % Lagrer frekvensene som faktisk er brukt
    f_analyse = f_analyse*ftrinn; % Beregner neste frekvens
  end;
  % Reduserer filstørrelse ved å fjerne mye av overflødig informasjon i tid.
  % Dette gjøres kun for at filstørrelsen på plottene skal bli håndterbar.
  P = floor((K*fs)/(24 * fmax)); % Tallet 24 kan endres ved behov
  TarBareMedHvertXITid = P % Skriver til skjerm (monitorering)
  NP = floor(N/P);
  AntallPktITid = NP % Skriver til skjerm (monitorering)
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
  %title(’Wavelet Power Spektrum’); % Velg denne når det er aktuelt,
  title(’Sqrt(Wavelet Power Spektrum)’); % men denne når sqrt blir brukt
  colorbar('location','southoutside');
  msg = 'Done!';