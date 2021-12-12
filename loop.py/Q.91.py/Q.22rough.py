a = "ABCD"
for i in range(4):
    if i==1:
        print(" ",end="")
    if i==3:
        print(" ",end="")
    for j in range(i+1):
        print(a[i],end=" ")
    print()