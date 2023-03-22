import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge

# Generowanie zbioru punktów
a = np.random.randint(0, 5)
x = np.random.normal(1, 1, 100)
y = a * x + 1 + np.random.normal(1, 0.5, 100)

# Wizualizacja wykresu
plt.scatter(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

X = np.column_stack((x, np.ones_like(x)))
y = y.reshape(-1, 1)

# Estymacja parametrów
alpha = 0.5
ridge = Ridge(alpha=alpha, fit_intercept=False)
ridge.fit(X, y)

a = ridge.coef_
a = a.flatten()
print(a)

# Dopasowanie krzywej
x_fit = np.linspace(np.min(x), np.max(x), 100)
y_fit = a[0] * x_fit + a[1]

# Wyświetlenie krzywej dopasowanej
plt.plot(x_fit, y_fit, color='r')

# Wizualizacja wykresu
plt.scatter(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
