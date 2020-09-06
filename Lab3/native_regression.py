import sys
from matrix import *
import matplotlib.pyplot as plt

data = loadtxt(sys.argv[1])


def main():
    Y2 = []
    Y = []
    X = []

    for i in data:
        X.append(i[0])
        Y.append(i[1])

    Xp = powers(X, 0, 1)
    Yp = powers(Y, 1, 1)
    Xpt = transpose(Xp)

    [[b], [m]] = matmul(invert(matmul(Xpt, Xp)), matmul(Xpt, Yp))

    for i in X:
        temp = b + (m * i)
        Y2.append(temp)

    plt.plot(X, Y, 'ro')
    plt.plot(X, Y2)
    plt.show()


main()
