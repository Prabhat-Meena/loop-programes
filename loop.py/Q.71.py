a = "ABCD"
for i in range(4,0,-2):
    for j in range(i):
        print(a[4-i+j],end="")
    for g in range(4-i-1):
        print(a[g],end="")
    print()
for i in range(2,0,-2):
    for j in range(i):
        print(a[j],end="")
    print()
    print("C",end="")
