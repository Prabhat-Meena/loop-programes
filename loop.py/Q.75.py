a = "abcde"
for i in range(1,6):
    for j in range(i):
        print(i-j,end="")
    for k in range(8-i):
        print(" ",end="")
    for m in range(1,i+1):
        print(a[i-m],end="")
    print()