import numpy as np


# the function of Perceptron
def perceptron(x1, x2, w1, w2, weight):
    input = np.array(x1, x2)
    weight = np.array(w1, w2)
    result = sum(input * weight)
    if result + weight > 0:
        return True
    else:
        return False


def orGate(x1, x2):
    return perceptron(x1, x2, 1, 1, 0.1)


print(orGate(0, 0))
