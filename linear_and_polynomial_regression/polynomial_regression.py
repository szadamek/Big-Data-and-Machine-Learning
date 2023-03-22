import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Generowanie zbioru punktów
a = np.random.randint(-5, 5)
b = np.random.randint(-5, 5)
c = np.random.randint(-5, 5)
x = np.random.normal(0, 1, 100)
print(x)
y = a * x * x * x + b * x * x + c * x + 1 + np.random.normal(0, 1.5, 100)


def polynomial(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 + c * x + d


# Przekształcenie danych
X = np.column_stack((x ** 3, x ** 2, x, np.ones_like(x)))
y = y.reshape(-1, 1)

# Obliczenie parametrów modelu
parameters = np.linalg.inv(X.T @ X) @ (X.T @ y)
a, b, c, d = parameters.flatten()

# Wypisanie wyników
print("Wartość współczynnika a: ", a)
print("Wartość współczynnika b: ", b)
print("Wartość współczynnika c: ", c)
print("Wartość współczynnika d: ", d)

# Wizualizacja danych
plt.scatter(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

plt.scatter(x, y)

# Dopasowanie krzywej
x_fit = np.linspace(np.min(x), np.max(x), 100)
y_fit = polynomial(x_fit, a, b, c, d)

# Wyświetlenie krzywej dopasowanej
plt.plot(x_fit, y_fit, color='r')
plt.xlabel("x")
plt.ylabel("y")
plt.show()
