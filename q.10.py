a = "ABCDE"
h = 0
while(h<5):
    g = 0
    while(g<=h):
        print(a[g],end="")
        g = g+1
    print()
    h = h+1


k = "ABC"
m = len(k)
i = 0
a = 1
p = 4
while i<m:
    j = 1
    d = 4
    while j<=a:
        print(k[d-p], end="")
        j=j+1
        d=d-1
    a=a+1
    print()
    i=i+1
    p=p-1

