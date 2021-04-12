x = list(range(1, 101))
i = int(0)
for i in x:
    if(i % 3 == 0 or i % 5 == 0):
        #i += 1
        # break
        # elif(i % 5 == 0):
        #i += 1
        continue
    elif(i % 2 != 0):
        print("pass")
        pass
    else:
        print(i)
#print("break at:", i-1)
print("Nothing to see here move along")
