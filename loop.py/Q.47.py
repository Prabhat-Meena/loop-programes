a = "ABCDEF"
for i in range(6,0,-1):
    for j in range(i):
        print(a[j],end="")
    #for g in range(4-i):
    #    print("_",end="")
    #for p in range(4-i):
    #    print("_",end="")
    for j in range(i):
        print(a[i-j-1],end="")
    print()