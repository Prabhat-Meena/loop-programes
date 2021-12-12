d = "ABCDE"
for i in range(9):
    if i<=4:
        for j in range(i+1):
            print(d[i-j],end="")
    else:
        for k in range(9-i):
            print(d[8-i-k],end='')
    print()
