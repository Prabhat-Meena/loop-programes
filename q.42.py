p2 = "ABCDE"
a = 5
i = 1
p = 0
while(p<=4):
    j = 1
    d = 5
    while(j<=a):
        print(p2[d-i],end="")
        j = j+1
        d = d-1
    a = a-1
    print()
    i = i+1
    p = p+1

