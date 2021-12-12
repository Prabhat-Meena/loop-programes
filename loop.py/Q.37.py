a = "ABCD"
for i in range(1,8):
    if i<=4:
        for d in range(4-i):
            print(" ",end="")
        for j in range(i):
            print(a[j],end="")
        for n in range(1,i):
            print(a[i-n-1],end="")
    else:
        for z in range(i-4):
            print(" ",end="")
        for k in range(8-i):
            print(a[k],end="")
        for m in range(1,8-i):
            print(a[7-i-m],end="")
    print()