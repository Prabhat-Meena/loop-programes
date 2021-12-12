


year= int(input("Enter your service years: "))
salry=int(input("Enter your salry"))
if year>10:
    bonus = salry*10/100 
    print('bonus',bonus)
elif year>=6 and year<=10:
    bonus = salry*8/100
    print('bonus',bonus)
elif year<6:
    bonus = salry*5/100
    print('bonus',bonus)
else:
    print('invalid')     
