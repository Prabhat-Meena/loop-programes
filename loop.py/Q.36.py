for i in range(1,8):
    if i<=4:
        for d in range(4-i):
            print(" ",end="")
        for j in range(i):
            print(j+1,end="")
        for n in range(1,i):
            print(i-n,end="")
    else:
        for z in range(i-4):
            print(" ",end="")
        for k in range(8-i):
            print(k+1,end="")
        for m in range(1,8-i):
            print(8-i-m,end="")
    print()