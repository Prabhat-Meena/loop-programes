i = int(input("Enter a number"))
a = 1
count = 0
while(a<=i):
    if i%a==0:
        count = count+1
    a = a+1
if count==2:
    print("prime number")
else:
    print("Not Prime")