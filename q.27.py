a = "ABCD"
z = len(a)
i = 0
while(i<=z-1):
    c = 0
    while(c<=i):
        print(a[i],end="")
        c = c+1
    i = i+1
    print()

al = "ABC"
j = len(al)
d = 2
i = 0
while(i<=j-1):
    c = 2
    while(c>=i):
        print(al[d],end="")
        c = c-1
    i = i+1
    print()
    d = d-1
