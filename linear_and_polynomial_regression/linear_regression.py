import numpy as np
import matplotlib.pyplot as plt

# Generowanie zbioru punktów
a = np.random.randint(0, 5)
x = np.random.normal(1, 1, 100)
y = a * x + 1 + np.random.normal(1, 0.4, 100)

# Wizualizacja wykresu
plt.scatter(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

X = np.column_stack((x, np.ones_like(x)))
y = y.reshape(-1, 1)
print(X)
print(y)

# Estymacja parametrów
parameters = np.linalg.inv(X.T @ X) @ (X.T @ y)
a, b = parameters.flatten()

# Dopasowanie krzywej
x_fit = np.linspace(np.min(x), np.max(x), 100)
y_fit = a * x_fit + b

# Wyświetlenie krzywej dopasowanej
plt.plot(x_fit, y_fit, color='r')

# Wizualizacja wykresu
plt.scatter(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
