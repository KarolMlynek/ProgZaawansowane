import numpy as np


def monte_carlo_integrate(f, a, b, n):
    x_random = np.random.uniform(a, b, n)
    f_values = f(x_random)
    mean_value = np.mean(f_values)
    integral = (b - a) * mean_value
    return integral



if __name__ == "__main__":
    def f(x):
        return x ** 2
    a = 0
    b = 1
    n = 10000
    result = monte_carlo_integrate(f, a, b, n)
    print(f"Przybliżona wartość całki: {result}")


