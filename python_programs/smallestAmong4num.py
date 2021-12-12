a = int(input("Enter a number"))
b = int(input("Enter a number"))
c = int(input("enter a number"))
d = int(input("Enter a number"))
if (a<b and a<c and a<d):
    print("A")
elif(b<a and b<c and b<d):
    print("B")
elif(c<a and c<b and c<d):
    print("C")
else:
    print("D")

