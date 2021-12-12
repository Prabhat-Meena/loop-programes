a = 1
for i in range(5,0,-1):
    for k in range(1,a):
        print(" ",end="")
    b = 0
    for j in range(i):
        print(a+b,end="")
        b = b+1
    d = 4
    for m in range(i-1):
        print(d-m,end="")
    a = a+1
    print()