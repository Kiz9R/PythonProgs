# pass by valur and pass by reference...
# pass by value:-
def update(x):
    x = 8
    print("x:", x)


a = 10
update(a)
print("a:", a)

# pass by reference:-


def update2(lst):
    lst[1] = 20
    print("lst update:", lst)


lst = [10, 25, 30]
update2(lst)
print("lst:", lst)
