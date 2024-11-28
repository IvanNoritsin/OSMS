import matplotlib.pyplot as plt
import numpy as np

probability_7bits = []
errors_7bits = []
probability_3bits = []
errors_3bits = []

with open('probability_7bits.txt', 'r') as file:
    for line in file:
        values = line.strip().split(',')
        probability_7bits.append(float(values[0]))
        errors_7bits.append(int(values[1]))
    
with open('probability_3bits.txt', 'r') as file:
    for line in file:
        values = line.strip().split(',')
        probability_3bits.append(float(values[0]))
        errors_3bits.append(int(values[1]))

    
plt.figure(figsize=(13, 10))
x = np.arange(1, 26, 1)
plt.plot(x, probability_7bits, label='7 bits')
plt.plot(x, probability_3bits, label='4 bits')
plt.legend()
plt.grid()
plt.xlabel("Размер массива * 100")
plt.xlim(1, 25)

plt.figure(figsize=(13, 10))
x = np.arange(1, 26, 1)
plt.plot(x, errors_7bits, label='7 bits')
plt.plot(x, errors_3bits, label='4 bits')
plt.legend()
plt.grid()
plt.xlabel("Размер массива * 100")
plt.ylabel("Пропущенных ошибок")
plt.xlim(1, 25)
