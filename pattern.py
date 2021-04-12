import math as m
b = input("Enter your name: ")
a = len(b)
k = int(0)
if (a % 2 != 0):
    c = m.ceil(a/2)
    for i in range(a):
        for j in range(0, a):
            if(j < c-k or j > c+k):
                print(b[j], end="")

            else:
                print(" ")
            k += 1
    print()
else:
    m1 = int(a/2)
    m2 = m1+1
    for i in range(a):
        for j in range(0, a):
            if(j < m1-k or j > m2+k):
                print(b[j], end="")
            else:
                print(" ")
            k += 1
    print()
