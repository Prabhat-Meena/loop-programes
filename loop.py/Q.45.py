for i in range(1,10,2):
    for d in range(9-i):
        print(" ",end="")
    for j in range(i):
        print(j+1,end=" ")
    print()