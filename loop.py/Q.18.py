for i in range(5,0,-1):
    for j in range(5-i):
        print(" ",end=" ")
    for k in range(i):
        print(k+1,end=" ")
    for k in range(1,i):
        print(i-k,end=" ")
    print()