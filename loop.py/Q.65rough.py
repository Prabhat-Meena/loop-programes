for i in range(1,4):
    for j in range(i):
        print(j+1,end="")
    for g in range(3-i):
        print("_",end="")
    for p in range(3-i):
        print("_",end="")
    for j in range(i):
        print(i-j,end="")
    if i==1:
        break
    print()