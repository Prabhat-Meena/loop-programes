d = 1
g = 1
for i in range(1,4):
    if d==5:
        for j in range(d+1):
            print(g,end=" ")
            g=g+2
    else:
        for k in range(d):
            print(g,end=" ")
            g=g+2
    d=d+2
    print()
    
