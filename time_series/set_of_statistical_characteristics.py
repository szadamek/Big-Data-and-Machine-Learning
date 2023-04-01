import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

t = pd.date_range(start='2021-01-01', end='2021-03-17', freq='H')
x = np.round(np.cumsum(np.random.normal(0, 1, size=(t.size)), axis=0), 2)

df = pd.DataFrame(x, index=t, columns=['x'])

# wyznaczenie wartości średniej i odchylenia standardowego
mean_val = np.sum(df['x']) / df['x'].size
std_val = np.sqrt(np.sum((df['x'] - mean_val) ** 2) / df['x'].size)

# wyznaczenie granic przedziałów odchylenia standardowego
k = 1  # liczba odchyleń standardowych od średniej
upper_bound = mean_val + k * std_val
lower_bound = mean_val - k * std_val

# minimum i maksiumum
min_val = np.min(df['x'])
max_val = np.max(df['x'])

# mediana bez funkcji
median = np.sort(df['x'])[df['x'].size // 2]

# kurtoza
kurtose = np.sum((df['x'] - mean_val) ** 4) / (df['x'].size * std_val ** 4) - 3
print(f'kurtoza = {kurtose}')
# kurtoza z biblioteki
kurtose_lib = df['x'].kurtosis()
print(f'kurtoza z biblioteki = {kurtose_lib}')

with plt.style.context('seaborn'):
    fig, ax = plt.subplots()
    df.plot(ax=ax)
    # resampling
    df.resample('D').mean().plot(ax=ax, linewidth=5)
    # linia średniej wartości
    ax.axhline(mean_val, color='red', linestyle='--', linewidth=2)
    # przedział górny odchylenia standardowego
    ax.fill_between(df.index, upper_bound, df['x'], where=df['x'] >= upper_bound, color='green', alpha=0.2)
    # przedział dolny odchylenia standardowego
    ax.fill_between(df.index, lower_bound, df['x'], where=df['x'] <= lower_bound, color='green', alpha=0.2)
    # punkt minimalny
    ax.scatter(df.index[df['x'] == min_val].to_pydatetime(), [min_val] * np.sum(df['x'] == min_val), color='purple',
               marker='o', s=100)
    # punkt maksymalny
    ax.scatter(df.index[df['x'] == max_val].to_pydatetime(), [max_val] * np.sum(df['x'] == max_val), color='purple',
               marker='o', s=100)
    # mediana
    ax.axhline(median, color='orange', linestyle='--', linewidth=2)
    # kurtoza
    ax.text(0.05, 0.95, f'kurtoza = {kurtose:.2f}', transform=ax.transAxes, fontsize=14, verticalalignment='top')
    # legenda
    ax.legend(['x', 'resampled x', 'mean', 'upper bound', 'lower bound', 'min', 'max', 'median'])
plt.show()
