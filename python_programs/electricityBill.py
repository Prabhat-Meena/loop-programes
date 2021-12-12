units = int(input('enter number of units consume'))
a = units*0
b = (units-100)*5
c = (units*10)-1500
if(units<=100):
    print("No charge", a)
elif(units>100 and units<=200):
    print("Your bill is",b)
else:
    print("your elecricity bill is", c)