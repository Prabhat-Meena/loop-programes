a = 5
i = 0
while(i<=4):
    b = 1
    while(b<=i):
        print("  ",end="")
        b = b+1
    j=1
    while(j<=a):
        print("#",end=" ")
        j = j + 1
    a = a-1
    print()
    i = i + 1

i = 1
while(i<=5):
    b=1
    while(b<=i):
        print("# ",end="")
        b = b+1
    i = i+1
    print()



# or

#i = 0
#a = 5
#while(i<=4):
#    print(" "*i,end="")
#    j=1
#    while(j<=1):
#        print("#"*a)
#        j = j+1
#    a = a-1
#    i = i+1
