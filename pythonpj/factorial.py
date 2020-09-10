def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def iterFactorial(n):
    a = 1

    for i in range(1, n + 1):
        a = a * i
    return a


def A(m, n):
    if m == 0:
        return n + 1
    if n == 0:
        return A(m - 1, 1)
    n2 = A(m, n - 1)
    return A(m - 1, n2)


def AutoAckerman():
    for i in range(1, 6):
        for j in range(1, 6):
            print(f"Ackermans formula of {i}, {j}")
            print(A(i, j))


AutoAckerman()