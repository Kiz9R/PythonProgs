# using filter(),map(),reduce() function....

from functools import reduce


def a(x):
    return x % 2 == 0


def b(x):
    return x*2


def c(x, x1):
    return x+x1


n1 = [1, 2, 3, 4, 5, 6]
even = list(filter(a, n1))
double = list(map(b, even))
sum = reduce(c, double)
print("filter:-", even)
print("map:-", double)
print("reduce:-", sum)

#  or


num = [11, 12, 13, 14, 15, 16]
evens = list(filter(lambda n: n % 2 == 0, num))
doubles = list(map(lambda e: e*2, evens))
sum1 = reduce(lambda r, r1: r + r1, doubles)
print("filter:-", evens)
print("map:-", doubles)
print("reduce:-", sum1)
