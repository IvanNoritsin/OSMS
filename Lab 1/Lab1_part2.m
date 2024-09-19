[y, Fs] = audioread('golos.wav');
y1 = downsample(y, 10);
zvuk = audioplayer(y1,Fs/10);
play(zvuk);
plot(y1);

Y = fft(y);
n = length(Y);
f = (0:n-1)*(Fs/n);
amplitudeY = abs(Y/n);

Y1 = fft(y1);
n1 = length(Y1);
f1 = (0:n1-1)*(Fs/10/n1);
amplitudeY1 = abs(Y1/n1);

figure;

subplot(2,1,1);
plot(f(1:floor(n/2)), amplitudeY(1:floor(n/2)));
xlabel('Частота (Гц)');
ylabel('Амплитуда');
title('Амплитудный спектр исходного сигнала');

subplot(2,1,2);
plot(f1(1:floor(n1/2)), amplitudeY1(1:floor(n1/2)));
xlabel('Частота (Гц)');
ylabel('Амплитуда');
title('Амплитудный спектр децимированного сигнала');