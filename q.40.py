a = "ABCDE"
h = 0
while(h<5):
    b = 4
    while(b>h):
        print(" ",end="")
        b = b-1
    g = 0
    while(g<=h):
        print(a[g],end="")
        g = g+1
    print()
    h = h+1

a = "ABCDE"
h = 4
while(h>=1):
    b = 4
    while(b>=h):
        print(" ",end="")
        b = b-1
    g = 0
    while(g<h):
        print(a[g],end="")
        g = g+1
    print()
    h = h-1