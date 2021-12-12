a = 1
y = 7
for i in range(1,5):
    z = y
    for b in range(i):
        print(z,end=" ")
        z=z+1
    y=y+y
    a=a+a
    i = a
    print()
