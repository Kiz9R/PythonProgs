# using filter() function


def a(x):
    return x % 2 == 0


n = [1, 2, 3, 4, 5, 6]
even = list(filter(a, n))
print(even)


#  or


num = [11, 12, 13, 14, 15, 16]
evens = list(filter(lambda x: x % 2 == 0, num))
print(evens)
