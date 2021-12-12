a = 1
for i in range(1,5):
    for g in range(5-i):
        print(" ",end="")
    for j in range(i):
        print(a,end=" ")
        a = a+1
    print()