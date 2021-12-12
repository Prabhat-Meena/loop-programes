a = 2
d = 1
for i in range(1,8):
    if i%2==0:
        s = 0
        for j in range(2):
            print(a+s,end="")
            s=s+1
        a=a+3       
    else:
        print(d,end="")
        d=d+3
    print()
