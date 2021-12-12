a = int(input("Enter a number: "))
if a%2==0 or a%3==0 or a%5==0:
    if(a==2 or a==3 or a==5):
        print(a, ":", "is a prime number")
    else:
        print(a, ":", "is not a prime number")
else:
    if a==1:
        print(a, ":"  "is not a prime number")
    else:
        print(a, ":", "is a prime number")
