n = 1
while (n<=1000):
    count = 0
    i = 1
    while (i<=n):
        if (n%i==0):
            count=count+1
        i=i+1
    if (count==2):
        print(n)
    n=n+1