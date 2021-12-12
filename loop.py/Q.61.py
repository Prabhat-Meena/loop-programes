a = 1
for i in range(5,0,-1):
    for k in range(5-i):
        print(" ",end="")
    b = 0
    for j in range(i):
        print(a+b,end=" ")
        b=b+1
    a=a+1
    print()