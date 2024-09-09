import numpy as np


# the function of Perceptron
def perceptron(x1, x2, w1, w2, bias):
    input = np.array([x1, x2])
    weight = np.array([w1, w2])
    result = sum(input * weight)
    if result + bias > 0:
        return True
    else:
        return False


def orGate(x1, x2):
    return perceptron(x1, x2, 1, 1, -0.1)


def nandGate(x1, x2):
    return perceptron(x1, x2, -0.5, -0.5, 0.7)


def andGate(x1, x2):
    return perceptron(x1, x2, 0.5, 0.5, -0.7)


def xorGate(x1, x2):
    s1 = nandGate(x1, x2)
    s2 = orGate(x1, x2)
    y = andGate(s1, s2)
    return y


for i in range(0, 2):
    for j in range(0, 2):
        print(i, j, xorGate(i, j))
