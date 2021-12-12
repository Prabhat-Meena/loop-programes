q = int(input("quantity"))
c = q*100
if c>1000:
    d = c*10/100
    t = c-d
    print("your total cost is", t)
else:
    print("you total cost is", c)