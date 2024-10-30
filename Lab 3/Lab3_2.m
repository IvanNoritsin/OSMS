a = [0.3, 0.2, -0.1, 4.2, -2, 1.5, 0];
b = [0.3, 4, -2.2, 1.6, 0.1, 0.1, 0.2];

figure;
subplot(2, 1, 1);
plot(a);
title('Массив a');
xlabel('Индекс');
ylabel('Значение');
grid on;

subplot(2, 1, 2);
plot(b);
title('Массив b');
xlabel('Индекс');
ylabel('Значение');
grid on;

corr = sum(a .* b);
norm_corr = corr / sqrt(sum(a.^2) * sum(b.^2));

fprintf('Корреляция между массивом a и массивом b: %f\n', corr);
fprintf('Нормализованная корреляция между массивом a и массивом b: %f\n', norm_corr);

num_shifts = length(b);
corr_shift = zeros(1, num_shifts);
norm_corr_shift = zeros(1, num_shifts);

for shift = 0:num_shifts-1
    b_shifted = circshift(b, shift);
    corr_shift(shift + 1) = sum(a .* b_shifted);
    norm_corr_shift(shift + 1) = sum(a .* b_shifted) / sqrt(sum(a .^2) * sum(b .^2));
end


figure;
plot(0:num_shifts-1, corr_shift);
title('Зависимость корреляции от величины сдвига');
xlabel('Сдвиг');
ylabel('Корреляция');
grid on;

figure;
plot(0:num_shifts-1, norm_corr_shift);
title('Зависимость нормализованной корреляции от величины сдвига');
xlabel('Сдвиг');
ylabel('Нормализованная корреляция');
grid on;

[max_corr, max_shift] = max(corr_shift);
max_shift = max_shift - 1;

figure;
subplot(2, 1, 1);
plot(a);
title('Массив a');
xlabel('Индекс');
ylabel('Значение');
grid on;

subplot(2, 1, 2);
plot(circshift(b, max_shift));
title('Массив b, сдвинутый для достижения максимальной корреляции');
xlabel('Индекс');
ylabel('Значение');
grid on;