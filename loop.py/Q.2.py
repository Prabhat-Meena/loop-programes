a = 5
for i in range(a,0,-1):
    for j in range(a-i):
        print(" ",end="")
    for d in range(i):
        print(i,end="")
    print()
