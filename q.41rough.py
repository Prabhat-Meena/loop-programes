ap2 = "ABCD"
a = 4
i = 1
p = 0
while(p<4):
    j = 1
    d = 4
    while(j<=a):
        print(ap2[d-i],end="")
        j = j+1
        d = d-1
    a = a-1
    print()
    i = i+1
    p = p+1