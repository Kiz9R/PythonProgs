n = range(2, 21)
s = str()
for i in n:
    if(i > 1):
        for j in range(2, i):
            if(i % j == 0):
                break
        else:
            s = s+' '+str(i)
print("The prine nos are:-", s)
