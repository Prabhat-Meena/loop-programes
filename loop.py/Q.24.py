a = "ABCDE"
for i in range(5,0,-1):
    if i==3:
        for l in range(2):
            print(" ",end=" ")
    if i==2:
        for k in range(2):
            print(" ",end=" ")
    if i==1:
        for m in range(4):
            print(" ",end=" ")
    for j in range(i):
        print(a[5-i+j],end=" ")
    for j in range(1,i):
        print(a[4-j],end=" ")
    print()
