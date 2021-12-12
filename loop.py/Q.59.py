z = "ABCDEF"
a = 1
for i in range(1,6,2):
    if i>1:
        for j in range(i-1):
            print(z[j],end="")
        print()
    for k in range(1,i+1):
        print(k,end="")
        a = a+1
    print()
