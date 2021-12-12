y = 1
for i in range(1,7):
    for j in range(6-i):
        print("#",end="")
    for k in range(1):
        print("*",end="")
    if i>1:
        for m in range(y):
            print("#" ,end="")
        for t in range(1):
            print("*",end="")
        y=y+2
    for g in range(6-i):
        print("#",end="")
    print()
