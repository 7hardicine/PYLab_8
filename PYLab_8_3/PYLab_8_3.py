from scipy import fsolve

def f(x):
    return x**2 - 5.8*x**3 - 4.2 * x**2 - 18.6 * x -3.6

koren = fsolve(f, )