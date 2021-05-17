def hi():
    print("hello world!")


hi()


def add(x, y):
    c = x+y
    print("the sum is:-", c)
    return c


add(4, 5)
ret = add(3, 4)
print("return value is:-", ret)


def mul_div(a, b):
    c = a*b
    d = a/b
    return c, d


res1, res2 = mul_div(9, 3)
print("the returned values are:-", res1, res2)

# anonymous function or function without name........


def d(x): return x*x


res0 = d(5)
print("the square of the numbers(check the code of the square):-", res0)
