
for i in range(1,10):
    print("*",end="")
    for j in range(2,i):
        print(" ",end="")
    if i>1 and i<10:
        print("*",end="")
    print()
    if i>8:
        for k in range(10):
            print("*",end="")
