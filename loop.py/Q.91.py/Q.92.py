for i in range(5,0,-1):
    for g in range(i-1):
        print(" ",end="")
    for k in range(6-i):
        print(i+k,end="")
    for m in range(5-i):
        print(4-m,end="")
    print()