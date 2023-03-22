import numpy as np
import matplotlib.pyplot as plt

# generowanie losowego szeregu czasowego
data = np.random.normal(loc=50, scale=10, size=100)

# wykres oryginalnego szeregu czasowego
plt.plot(data)
plt.title("Oryginalny szereg czasowy")
plt.show()

# standaryzacja szeregu czasowego
mean = np.mean(data)
std = np.sqrt(sum((data - mean) ** 2) / len(data))
data_std = (data - mean) / std

# wykres zstandaryzowanego szeregu czasowego
plt.plot(data_std)
plt.title("Zstandaryzowany szereg czasowy")
plt.show()
