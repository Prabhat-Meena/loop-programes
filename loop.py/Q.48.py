a = 1
for i in range(1,10,2):
    for d in range(9-i):
        print(" ",end="")
    for j in range(i):
        print(a,end=" ")
    a=a+1
    print()