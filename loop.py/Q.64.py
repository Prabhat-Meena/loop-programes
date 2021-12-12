q = 0
p = 5
for a in range(1,5):
    d = 6
    for j in range(a):
        print(d-p,end="")
        d = d+1
    g = 0
    for k in range(1,a):
        print(q-g,end="")
        g=g+1
    a=a+1
    print()
    p=p-1
    q=q+2
