import numpy as np
import matplotlib.pyplot as plt

R = lambda x: np.sin(2 * x) / (1 + x ** 2)
# R = lambda x: 1 + x + x ** 2 + x ** 3

Nsamples = 4
# próbkowanie z oryginalnej funkcji R
x = np.linspace(0, 2, Nsamples)
y = R(x)

# Gdy punkty nie są posortowane, to nie można wykonać interpolacji
# W tym przypadku są posortowane od początku
sort = np.argsort(x)
x = x[sort]
y = y[sort]
print(sort)

# Interpolacja wielomianowa trzeciego stopnia
coefficients = np.polyfit(x, y, 3)
interpolation_function = np.poly1d(coefficients)

# Wartość interpolacji
x_intercept = float(input("Podaj punkt do interpolacji: "))
y_intercept = interpolation_function(x_intercept)
print(f'Wartość interpolacji dla punktu {x_intercept} wynosi {y_intercept}')

# Wygląd funkcji
x_function = np.linspace(0, 2)
y_function = R(x_function)

plt.plot(x_function, y_function, "--", color='green')
plt.plot(x_function, interpolation_function(x_function), label='Interpolacja')
plt.scatter(x, y)
plt.legend()
plt.show()
