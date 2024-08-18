import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# функція
def f(x):
    return -x**2 + 3*x - 2

# Метод Монте-Карло 
def monte_carlo_integral(a, b, num_points=10000):
    # Генерація випадкових x-координат
    x_random = np.random.uniform(a, b, num_points)
    
    y_min = min(f(np.linspace(a, b, 1000)))
    y_max = max(f(np.linspace(a, b, 1000)))
    
    y_random = np.random.uniform(y_min, y_max, num_points)
    
    points_under_curve = np.sum(y_random <= f(x_random))
    
    area = (b - a) * (y_max - y_min) * (points_under_curve / num_points)
    return area

# Границі інтегрування
a, b = 1, 2

# Результат методом Монте-Карло
monte_carlo_result = monte_carlo_integral(a, b)
print(f"Значення інтегралу методом Монте-Карло: {monte_carlo_result}")


# Обчислення аналітичного значення
analytical_result, _ = quad(f, a, b)
print(f"Аналітичне значення інтегралу: {analytical_result}")

# похибка
error = abs(analytical_result - monte_carlo_result)
print(f"Похибка методу Монте-Карло: {error:.6f}")

# Візуалізація
x = np.linspace(a, b, 400)
y = f(x)
plt.plot(x, y, label='-x^2 + 3x - 2')

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)


plt.fill_between(x, y, alpha=0.2, color='gray')
plt.legend()
plt.show()
