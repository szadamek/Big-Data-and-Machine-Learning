import numpy as np
import matplotlib.pyplot as plt


def linear_interpolation(x, y, x_interp):
    '''Funkcja interpolująca'''
    if x[0] > x_interp and x[-1] < x_interp:
        return None
    idx = None
    for i in range(len(x) - 2):
        if x[i] < x_interp and x[i + 1] > x_interp:
            idx = i
            break

    if idx is None:
        return None

    xA, yA = x[idx], y[idx]
    xB, yB = x[idx + 1], y[idx + 1]
    a = (yB - yA) / (xB - xA)
    b = yA - a * xA
    return a * x_interp + b


R = lambda x: np.sin(2 * x) / (1 + x ** 2)

Nsamples = 12
# próbkowanie z oryginalnej funkcji R
x = np.linspace(0, 2, Nsamples)
y = R(x)

# Gdy punkty nie są posortowane, to nie można wykonać interpolacji
# W tym przypadku są posortowane od początku
sort = np.argsort(x)
x = x[sort]
y = y[sort]
print(sort)

x_input = float(input("Podaj punkt do interpolacji: "))
y_input = linear_interpolation(x, y, x_input)
if y_input is None:
    print(f'Punkt {x_input} znajduje się poza zakresem interpolacji')
else:
    print(f'Wartość interpolacji dla punktu {x_input} wynosi {y_input}')

# Wygląd funkcji
x_function = np.linspace(0, 2)
y_function = R(x_function)

plt.plot(x_function, y_function, "--", color='green')
for i in range(len(x) - 1):
    plt.plot([x[i], x[i + 1]], [y[i], y[i + 1]], color="orange")
plt.scatter(x, y)
plt.show()
