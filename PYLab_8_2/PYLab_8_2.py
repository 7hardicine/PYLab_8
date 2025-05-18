from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt

def f1pr(x):
    return -(np.sqrt(2)*(6*x**2-5))/(np.sqrt(25-15*x**2))
def f2pr(x):
    return -(np.sqrt(5)*(3*x**2-4*x))/(np.sqrt(10-6*x))
def integralf1(x):
    return np.sqrt(1 + f1pr(x)**2)
def integralf2(x):
    return np.sqrt(1 + f2pr(x)**2)

x0 = 0
xf = 1.01
dx = 0.01

X = np.arange(x0, xf, dx)
F1 = X * np.sqrt(2 - 1.2* X**2)
F2 = X**2 * np.sqrt(2 - 1.2 * X)

len1 = quad(integralf1, x0, xf)[0]
print("Длина первого пути: ", len1)
len2 = quad(integralf2, x0, xf)[0]
print("Длина второго пути: ", len2)

if len1 < len2:
    print('Первый путь кратчайший')
elif len2 < len1:
    print('Второй путь кратчайший')
else:
    print('Пути равны')

plt.figure()
plt.plot(X, F1, '--r')
plt.scatter(X, F1, color = 'blue')
plt.scatter(X, F2, color = 'yellow')
plt.plot(X, F2, '--k')
plt.grid()
plt.legend(['Первый путь', 'точки первого пути', 'точки второго пути', 'Второй путь'])
plt.show()

