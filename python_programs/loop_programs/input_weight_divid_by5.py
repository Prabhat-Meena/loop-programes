a = 0
i = 1
while(i<=11):
    weight = int(input("Enter your weight: "))
    a = a+weight/11
    print(a)
    i = i+1
if a%5==0:
    print("yes")
else:
    print("no")