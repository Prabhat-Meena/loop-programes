#i = 1
#while(i<=3):
#    if (i>3 and i<6):
#        print('*'*6,end='')
#    else:
#        b = 1
#        while(b<=i):
#            print('*',end='')
#            b = b+1
#    print()
#    i = i+2



i = 1
d = 1
#g = 1
while(i<=3):
    if d == 5:
        b = 1
        while(b<=d+1):
            print("*",end='')
            b = b+1
            #g = g+2
    else:
        b = 1
        while(b<=d):
            print("*",end="")
            b = b+1
            #g = g+2
    i = i+1
    d  = d+2
    print()
