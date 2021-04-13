import array as arr
v = arr.array('i', [])
n = int(input("Enter the length of the array:-"))
for i in range(n):
    x = int(input("Enter the elements:-"))
    v.append(x)
for i in range(n):
    print(v[i], ' ', end="")

s = int(input("\nEnter the value u want to search:-"))
for i in range(n):
    if(s == v[i]):
        print("Value found at ", i)
        break
else:
    print("value not found")
