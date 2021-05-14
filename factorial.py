# printing factorial of a number of

def fact(x):
    a = 1
    for i in range(1, x+1):
        print(i, "!", " ", end="")
        a *= i
    print("\nthe factorial of the number is:-", a)


x = (int(input("enter the number:-")))

fact(x)
