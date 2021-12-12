a = 0
i = 100
while(i<=400):
    a = str(i)
    if int(a[0])%2==0 and int(a[1])%2==0 and int(a[2])%2==0:
        print(a,",",end=" ")
    i = i+1