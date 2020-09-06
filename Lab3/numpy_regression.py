
import sys
import matplotlib.pyplot as plt
from numpy import *


def poly(a, x):
    y = a[0]
    for i in range(len(a) - 1):
        y = y + a[i + 1] * x ** (i + 1)
    return y


def powers(m, p1, p2):
    result = []

    if m == result:
        return m
    else:
        for i in range(len(m)):
            r2 = []
            for j in range(p1, p2 + 1):
                val = m[i] ** j
                r2.append(val)

            result.append(r2)

    return array(result)


data = loadtxt(sys.argv[1])
polyDegree = int(sys.argv[2])


def main():
    X = []
    Y = []
    Y2 = []
    for i in data:
        X.append(i[0])
        Y.append(i[1])

    print(Y)

    xMin = X[0]
    xMax = X[-1]

    n = int((xMax - xMin) / 0.2)
    X2 = linspace(xMin, xMax, n).tolist()

    Xp = powers(X, 0, polyDegree)
    Yp = powers(Y, 1, 1)
    Xpt = Xp.transpose()

    a = matmul(linalg.inv(matmul(Xpt, Xp)), matmul(Xpt, Yp))
    a = a[:, 0]

    for i in X2:
        temp = poly(a, i)
        Y2.append(temp)

    plt.plot(X, Y, 'ro')  # known values
    plt.plot(X2, Y2)  # prediction line
    plt.show()


main()
