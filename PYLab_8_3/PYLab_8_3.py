from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**4 - 5.8 * x**3 - 4.2 * x**2 - 18.6 * x - 3.6

def bisect(xn, xk, dx, eps):
    while xk - xn > eps:
       dx = (xk - xn)/2;
       xi = xn + dx;
       if (f(xn)<0 and f(xi)>0) or (f(xn)>0 and f(xi)<0):
           xk = xi
       else:
           xn = xi
    print (xi)

solution = fsolve(f, [5, 8])[0]
print(solution)

bisect(5,8,0.1,1e-8)


X = np.arange(5,8,0.1)
Y = f(X)
Yzeros = np.zeros(30)

plt.figure()
plt.grid()
plt.plot(X, Y, "--")
plt.plot(X, Yzeros, "g")
plt.plot(solution, 0, "*r")
plt.legend(["График функции", "Ось OX", "Нуль фукнции"])
plt.show()
