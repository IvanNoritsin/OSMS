f1 = 12;
f2 = 16;
f3 = 25;
t = (0:100)/100;

s1 = cos(2 * pi * f1 * t);
s2 = cos(2 * pi * f2 * t);
s3 = cos(2 * pi * f3 * t);

a = 4 * s1 + 4 * s2 + s3;
b = 2 * s1 + s2 + 2 * s3;

figure;
subplot(3, 1, 1);
plot(s1);
xlim([1, 101]);
title('Сигнал s1');
xlabel('t');
ylabel('A');
grid on;

subplot(3, 1, 2);
plot(a);
xlim([1, 101]);
title('Сигнал a');
xlabel('t');
ylabel('A');
grid on;

subplot(3, 1, 3);
plot(b);
xlim([1, 101]);
title('Сигнал b');
xlabel('t');
ylabel('A');
grid on;

corr_s1a = sum(s1 .* a);
corr_s1b = sum(s1 .* b);
norm_corr_s1a = corr_s1a / sqrt(sum(s1.^2) * sum(a.^2));
norm_corr_s1b = corr_s1b / sqrt(sum(s1.^2) * sum(b.^2));

fprintf('Корреляция между сигналом s1 и сигналом a: %f\n', corr_s1a);
fprintf('Корреляция между сигналом s1 и сигналом b: %f\n', corr_s1b);
fprintf('Нормализованная корреляция между сигналом s1 и сигналом a: %f\n', norm_corr_s1a);
fprintf('Нормализованная корреляция между сигналом s1 и сигналом b: %f\n', norm_corr_s1b);

