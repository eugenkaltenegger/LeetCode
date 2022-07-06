import math


def recursion(stairs: int):
    if stairs == 0:
        return 0
    if stairs == 1:
        return 1
    if stairs == 2:
        return 2
    return recursion(stairs - 1) + recursion(stairs - 2)


def loop(stairs: int):
    if stairs == 0:
        return 0
    ones_start = stairs % 2
    ones = list(range(stairs, ones_start-1, -2))
    twos_end = int(stairs / 2)
    twos = list(range(0, twos_end+1, 1))
    total = 0
    for n, k in zip(ones, twos):
        total += binomial_coefficient(n+k, k)
    return total


def formula(stairs: int):
    if stairs == 0:
        return 0
    return int(sum([math.factorial(stairs - n) / (math.factorial(stairs - 2 * n) * math.factorial(n)) for n in range(int(stairs / 2) + 1)]))


def binomial_coefficient(n: int, k: int):
    return int(math.factorial(n) / (math.factorial(n-k) * math.factorial(k)))


if __name__ == "__main__":
    stairs = 10
    print("number of stairs: {}".format(stairs))
    print("recursion: {}".format(recursion(stairs)))
    print("loop: {}".format(loop(stairs)))
    print("formula: {}".format(formula(stairs)))
