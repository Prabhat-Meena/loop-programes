i = 0
while(i<5):
    print(""*(4-i),end="")
    j = 0
    k = 1
    while(j-1<i*2):
        if j+1>i+1:
            print((i*2)-j+1,end="")
        #else:
        #    print(k,end="")
        k=k+1
        j = j+1
    print()
    i = i+1