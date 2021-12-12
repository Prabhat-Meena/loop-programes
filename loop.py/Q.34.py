#for i in range(1,8,2):
#    for j in range(8-i):
#        print(" ",end="")
#    for d in range(i):
#        print("#",end=" ")
#    print()

a = 5
#b = 1
for i in range(1,15,2):
    for d in range(7-i):
        print(" ",end="")
    if i<=8:
        for j in range(i):
            print("#",end=" ")
    else:
        for z in range(i-7):
            print(" ",end="")
        for k in range(a):
            print("#",end=" ")
        #b = b+1
        a = a-2
    print()



