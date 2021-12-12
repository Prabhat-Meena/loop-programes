a = int(input("Enter your age"))
b = int(input("Enter your age"))
c = int(input("Enter your age"))
if (a>b and a>c):
    print("a is oldest")
    if (b<c):
        print("b is youngest")
    else:
        print("c is youngest")
elif (b>a and b>c):
    print("b is oldest")
    if (a<c):
        print("a is youngest")
    else:
        print("c is youngest")
elif (c>a and c>b):
    print("c is oldest")
    if (b<a):
        print("b is youngest")
    else:
        print("a is youngest")
