d = "ABCDE"
for i in range(5,0,-1):
    if i>=1:
        for j in range(1,i+1):
            print(d[i-j],end="")
    print()
