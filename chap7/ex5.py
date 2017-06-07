import math
def sum_term(k):
    x = ((math.factorial(4 * k)) * (1103 + 26390 * k)) / (((math.factorial(k)) ** 4) * (396 ** (4 * k)))
    return x
def estimate_pi():
    const = (2 * (math.sqrt(2)) / 9801)
    sum_m = 0
    k = 0
    while (sum_term(k) > 1e-15):
        sum_m = sum_m + sum_term(k)
        k = k + 1
    return(1 / (const * sum_m))
print(estimate_pi())
