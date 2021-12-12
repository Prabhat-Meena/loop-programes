sum = 0
i = 1
while i<=11:
    a = int(input("Enter a number"))
    sum=sum+a
    print(sum)
    i = i+1
    b =sum/11
    print(b)
if b%5==0:
    print("divide")
else:
    print("no divide")
