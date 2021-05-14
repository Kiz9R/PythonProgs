# finding even or odd no using function
def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd


lst = []
n = (int(input("input a limit of list:")))
for i in range(0, n):
    a = (int(input("enter the numbers:")))
    lst.append(a)
#list = lst.split()

even, odd = count(lst)
print("Even : {} , Odd : {}".format(even, odd))
