z = "ABCDEF"
a = 1
for i in range(1,6,2):
    if i>1:
        for j in range(1,i):
            print(z[i+j-4],end="")
        print()
    for k in range(i):
        print(a,end="")
        a = a+1
    print()
