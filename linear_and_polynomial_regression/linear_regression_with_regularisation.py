import numpy as np
import matplotlib.pyplot as plt

# Generowanie zbioru punktów
x = np.random.normal(1, 1, 100)
y = 2 * x + 1 + np.random.normal(1, 0.5, 100)

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
alpha = 0.1
parameters = np.linalg.inv(X.T @ X + alpha * np.eye(X.shape[1])) @ X.T @ y
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
