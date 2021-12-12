a = "ABCD"
for i in range(4,0,-1):
    for d in range(4-i):
        print(" ",end="")
    for j in range(i):
        print(a[j],end="")
    for n in range(1,i):
        print(a[i-n-1],end="")
    print()