d = 9
for i in range(1,5,):
    for j in range(1):
        print(d,end="")
        d=d-1
    if i>1:
        c = d-1
        for k in range(1):
            print(c+3,end="")
    if i>2:
        y = c-2
        for t in range(1):
            print(y+6,end="")
    if i==4:
        print(9,end="")
    #print()
    for g in range(1,i):
        print(9-g,end="")
    print()



    
    