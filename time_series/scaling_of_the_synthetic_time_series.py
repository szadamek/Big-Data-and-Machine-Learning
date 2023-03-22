import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import torch

# Wczytanie szeregu czasowego
df = pd.read_csv('LBMA-GOLD.csv', nrows=100)
df['Date'] = pd.to_datetime(df['Date'])  # zmiana typu danych kolumny 'Date'
df.set_index('Date', inplace=True)  # ustawienie kolumny 'Date' jako indeks
X = df['USD (AM)'].values
print(X)

# Tworzenie szeregu syntetycznego
synthetic_X = []
# Tworzenie wektora szumu o wymiarze wektora X i rozkładzie normalnym, wykorzystując moduł torch z biblioteki PyTorch.
# Użyta funkcja torch.randn_like zwraca tensor o tym samym rozmiarze co X, wypełniony losowymi wartościami z rozkładu normalnego.
noise = torch.randn_like(torch.Tensor(X))
for i in range(len(X)):
    point = 0.3 * X[i - 1] + 0.2 * X[i] + 0.5 * noise[i]
    synthetic_X.append(point)
    print(f'x{i} = {point}')
synthetic_X = np.array(synthetic_X)

# Skalowanie szeregów
X_min = min(X)
X_max = max(X)
X_min_synthetic = min(synthetic_X)
X_max_synthetic = max(synthetic_X)
X = (X - X_min) / (X_max - X_min)
synthetic_X = (synthetic_X - X_min_synthetic) / (X_max_synthetic - X_min_synthetic)

# Tworzenie wykresu
plt.plot(df.index, X, label='Szereg oryginalny')  # przekazanie indeksu jako argumentu x
plt.plot(df.index, synthetic_X, label='Szereg syntetyczny')  # przekazanie indeksu jako argumentu x
plt.legend()
plt.show()
