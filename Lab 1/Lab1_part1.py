import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 1000)
A = 7
f = 16
ph = np.pi / 13

y = A * np.cos(2 * np.pi * f * t + ph)

plt.figure(figsize=(10, 6))
plt.plot(t, y)
plt.title(r'$y(t) = 7\cos(2\pi f t + \frac{\pi}{13}),\ f=16$')
plt.xlabel('Время (с)')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.show()

fs = 32
t_disc = np.arange(0, 1, 1 / fs)
y_disc = A * np.cos(2 * np.pi * f * t_disc + ph)

Y = np.fft.fft(y_disc)
N = len(Y)
frequencies = np.fft.fftfreq(N, 1/fs)
max_frequency = np.max(np.abs(Y))
print("Ширина спектра:", max_frequency)

memory_usage = y_disc.nbytes
print("Объем памяти:", memory_usage, "байт")

plt.figure(figsize=(10, 6))
plt.plot(t_disc, y_disc)
plt.title('Восстановленный сигнал')
plt.xlabel('Время (с)')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(t_disc, y_disc)
plt.plot(t, y, linestyle='--')
plt.xlabel('Время (с)')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.show()

