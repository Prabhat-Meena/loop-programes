for i in range(3,0,-1):
    if i==1:
        break
    for j in range(i):
        print(j+1,end="")
    for g in range(2-i):
        print("_",end="")
    for p in range(3-i):
        print("_",end="")
    for j in range(2):
        print(2-j,end="")
    print()
for i in range(1,4):
    for j in range(i):
        print(j+1,end="")
    for g in range(2-i):
        print("_",end="")
    for p in range(3-i):
        print("_",end="")
    if i>1:
        for j in range(2):
            print(2-j,end="")
    else:
        print(i,end='')
    print()
