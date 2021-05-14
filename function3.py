# passing multiple values through function

def sum(*b):
    c = 0
    for i in b:
        c = c+i
        print(c)
        print(i)
    print("the sum is:-", c)


def person(**data):

    for i, j in data.items():
        print(i, j)


sum(5, 6, 7, 8)
person(name='Kiz9r', age=20, city='Kolkata')
