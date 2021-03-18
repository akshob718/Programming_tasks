import numpy as np
import matplotlib.pyplot as plt
from random import random, randint
import math


def midpoint(p, q):
    return (0.5 * (p[0] + q[0]), 0.5 * (p[1] + q[1]))


corner = [(0, 0), (0.5, math.sqrt(3) / 2), (1, 0)]

N = 500
x = np.zeros(N)
y = np.zeros(N)


x[0] = random()
y[0] = random()
for i in range(1, N):
    k = randint(0, 2)
    x[i], y[i] = midpoint(corner[k], (x[i - 1], y[i - 1]))
    if i >= 100 and i % 100 == 0:
        #print(i)
        plt.title('Intermediate Sierpinski triangle after %i iterations' % i)
        plt.scatter(x, y)
        plt.show()

plt.scatter(x, y)
plt.title("Sierpinski triangle after complete %i iterations" % N)
plt.show()