import math
import random
from tabulate import tabulate
def square_root(a):
    b = random.randint(1,a)
    while True:
        y = (b + a / b) / 2
        if (y == b):
            return y
        b = y
def test_square_root():
    c = 0
    u = []
    for i in range(9):
        c = c + 1
        q = square_root(int(c))
        l = [c,q,math.sqrt(c),math.sqrt(c) - q]
        u.append(l)
    k = tabulate(u)
    print(k)
test_square_root()
