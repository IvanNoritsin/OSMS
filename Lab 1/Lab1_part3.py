import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

f = 16
A = 7
phi = np.pi / 13
T = 1
Fs = 512
t = np.linspace(0, T, Fs, endpoint=False)
y = A * np.cos(2 * np.pi * f * t + phi)

def quantize_signal(signal, bit_depth):
    levels = 2**bit_depth - 1
    quantized_signal = np.round(signal / A * levels) / levels * A
    quantized_signal = np.clip(quantized_signal, -A, A)
    return quantized_signal

def quantization_error(original_signal, quantized_signal):
    return np.mean(np.abs(original_signal - quantized_signal))

def compute_fft(signal):
    N = len(signal)
    yf = fft(signal)
    xf = fftfreq(N, 1 / Fs)
    return xf[:N//2], np.abs(yf[:N//2]) / N

def plot_spectrums(xf, yf_original, yf_quantized, bit_depth):
    plt.figure(figsize=(10, 6))
    plt.plot(xf, yf_original, label='Исходный сигнал')
    plt.plot(xf, yf_quantized, label=f'Квантованный сигнал ({bit_depth} бит)', linestyle='--')
    plt.title(f"Спектры сигнала для разрядности АЦП: {bit_depth} бит")
    plt.xlabel('Частота (Гц)')
    plt.ylabel('Амплитуда')
    plt.legend()
    plt.grid(True)
    plt.show()

bit_depths = [3, 4, 5, 6]
errors = []

xf, yf_original = compute_fft(y)

for bit_depth in bit_depths:
    y_quantized = quantize_signal(y, bit_depth)
    _, yf_quantized = compute_fft(y_quantized)
    error = quantization_error(y, y_quantized)
    errors.append(error)
    plot_spectrums(xf, yf_original, yf_quantized, bit_depth)
print(errors)