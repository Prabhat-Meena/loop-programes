for i in range(1,8):
    if i<=4:
        for d in range(4-i):
            print(" ",end="")
        for j in range(i):
            print(i-j,end="")
        for n in range(1,i):
            print(n+1,end="")
    else:
        for z in range(i-4):
            print(" ",end="")
        for k in range(8-i):
            print(8-i-k,end="")
        for m in range(1,8-i):
            print(m+1,end="")
    print()