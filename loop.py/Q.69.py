a = "ABCD"
for i in range(4,0,-1):
    for j in range(i):
        print(a[4-i+j],end="")
    for g in range(4-i):
        print(a[g],end="")
    print()