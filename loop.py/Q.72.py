a = 1
for i in range(1,5):
    for j in range(i):
        print(a,end=" ")
        a = a+1
        if a==10:
            print(1,end=" ")
            break
    print()
for g in range(2,7):
    print(g,end=" ")