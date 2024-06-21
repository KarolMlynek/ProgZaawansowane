import numpy as np


def monte_carlo_integrate_2d(f, ax, bx, ay, by, n):

    x_random = np.random.uniform(ax, bx, n)
    y_random = np.random.uniform(ay, by, n)

    f_values = f(x_random, y_random)

    mean_value = np.mean(f_values)

    integral = (bx - ax) * (by - ay) * mean_value
    return integral

if __name__ == "__main__":
    def f(x, y):
        return x ** 2 + y ** 2

    ax = 0
    bx = 1
    ay = 0
    by = 1

    n = 10000

    result = monte_carlo_integrate_2d(f, ax, bx, ay, by, n)

    print(f"Przybliżona wartość podwójnej całki: {result}")

