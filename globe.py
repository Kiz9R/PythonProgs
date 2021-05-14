# using global varriables

a = 10
b = 9


def any():
    a = 15
    b = 14
    print("inside function", a, b)
    print("id of in function a:-", id(a))
    print("id of in function b:-", id(b))

    x = globals()['a']
    print("id of x", id(x))


any()
print("global", a, b)
print("id of global a:-", id(a))
print("id of global b:-", id(b))
