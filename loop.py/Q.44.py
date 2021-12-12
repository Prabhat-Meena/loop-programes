for i in range(4,0,-1):
    for j in range(i):
        print(j+1,end="")
    for g in range(4-i):
        print("_",end="")
    for p in range(4-i):
        print("_",end="")
    for j in range(i):
        print(i-j,end="")
    print()