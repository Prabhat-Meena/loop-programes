d = "INDIA"
a = 5
for i in range(1,11):
    if i<=5:
        for j in range(i):
            print(d[j],end="")
    else:
        for k in range(a):
            print(d[k],end='')
        a = a-1
    print()
