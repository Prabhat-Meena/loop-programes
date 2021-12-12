a = "ABCD"
b = 3
for i in range(7):
    if i<4:
        for j in range(i+1):
            print(a[i],end="")
    else:
        for k in range(b):
            print(a[b-1],end='')
        b = b-1
    print()