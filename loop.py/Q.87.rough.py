for i in range(1,9):
    if i<=4:
        for j in range(i):
            print(i,end="")
            if j<i-1:
                print("*",end="")
    else:
        for k in range(9-i):
            print(9-i,end="")
            if k<8-i:
                print("*",end="")
    print()