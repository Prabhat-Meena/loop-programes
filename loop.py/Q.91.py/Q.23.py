a = "ABCDE"
y = 1
for i in range(5):
    if y<=2:
        for v in range(5):
            print(" ",end="")
        y=y+1
    else:
        if i>2 and i<4:
            print(" ",end="")
        elif i>2 and i<4:
            print(" ",end="")
    for j in range(i+1):
        print(a[j],end=" ")
    for k in range(1,i+1):
        print(a[i-k],end=" ")
    print()