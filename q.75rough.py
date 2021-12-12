al = "ABCDE"
a = 1
i = 0
p = 5
while a<=5:
    j = 1
    d = 5
    while(j<=a):
            print(al[d-p],end="")
            j = j+1
            d = d-1
    a = a+1
    print()
    p = p-1
    i = i +1

