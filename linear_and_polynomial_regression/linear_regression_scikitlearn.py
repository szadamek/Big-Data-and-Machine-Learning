import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

a = np.random.randint(0, 5)
x = np.random.normal(1, 1, 100)
y = a * x + 1 + np.random.normal(1, 0.4, 100)

# Wizualizacja danych - wykres
plt.scatter(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# Model regresji lin
model = LinearRegression()

X = x.reshape(-1, 1)

print(X)
print(y)
# Trenowanie modelu
model.fit(X, y)

# Wartości współczynników a i b
b = model.intercept_
a = model.coef_[0]
print(a, b)

# Wizualizacja wykresu
plt.scatter(x, y)
plt.plot(x, model.predict(X), color='r')
plt.xlabel("x")
plt.ylabel("y")
plt.show()
