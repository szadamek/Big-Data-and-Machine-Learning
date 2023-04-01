import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from nolds import corr_dim, hurst_rs, sampen


def fractal_dimension(X):
    # podział sygnału na przedziały o równej długości
    n = 10
    X_min = np.min(X)
    X_max = np.max(X)
    delta_X = (X_max - X_min) / n

    # policzenie liczby pudełek potrzebnych do pokrycia każdego przedziału
    counts = np.zeros(n)
    for i in range(n):
        box_min = X_min + i * delta_X
        box_max = X_min + (i + 1) * delta_X
        counts[i] = np.sum((X >= box_min) & (X <= box_max))

    # policzenie liczby pudełek potrzebnych do pokrycia całego sygnału dla każdego rozmiaru pudełka
    box_sizes = np.power(2, np.arange(1, np.floor(np.log2(n)) + 1))
    N = np.zeros_like(box_sizes)
    for i, size in enumerate(box_sizes):
        n_boxes = int(np.floor(n / size))
        if n_boxes == 0:
            break
        Xb = counts[:int(n_boxes * size)]
        Xb = np.reshape(Xb, (n_boxes, int(size)))
        N[i] = np.sum(np.sum(Xb, axis=1) > 0)

    # dopasowanie prostej
    coeff = np.polyfit(np.log(box_sizes[:i]), np.log(N[:i]), 1)
    D = coeff

    return D


t = pd.date_range(start='2021-01-01', end='2021-03-17', freq='H')
#x = np.round(np.cumsum(np.random.normal(0, 1, size=(t.size)), axis=0), 2)
x = np.round(np.random.normal(0, 1, size=(t.size)), 2)
df = pd.DataFrame(x, index=t, columns=['x'])

# entropia
entropia = -np.sum(df['x'] * np.log2(df['x']))
print(f'entropia = {entropia}')

# entropia z biblioteki nolds
entropia_nolds = sampen(df['x'].values)
print(f'entropia z nolds = {entropia_nolds}')

# wykładnik Hursta
H = hurst_rs(df['x'].values)
print(f'wykładnik Hursta = {H}')

# wymiar fraktalny
# https://en.wikipedia.org/wiki/Fractal_dimension
D = fractal_dimension(df['x'].values)
print(f'wymiar fraktalny = {-D[0]}')

# wymiar fraktalny z biblioteki nolds
D_nolds = corr_dim(df['x'].values, 10)
print(f'wymiar fraktalny z nolds = {D_nolds}')


with plt.style.context('seaborn'):
    fig, ax = plt.subplots()
    df.plot(ax=ax)
plt.show()
