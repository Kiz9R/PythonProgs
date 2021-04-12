import sys as s
check = int(s.argv[1])
#check = int(input("enter a check value"))
if (check < 2):
    a = int(input("enter a number:-"))
    b = int(input("enter another number:-"))
    if (check == 1):
        x = a+b
        print("the sum is:-", x)

    elif (check == 0):
        a, b = b, a
        print("swaped values are:-")
        print("a=", a)
        print("b=", b)
else:
    print("wrong input")
