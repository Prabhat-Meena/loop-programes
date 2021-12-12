day = int(input("accept the name day of charge"))
if day<=5:
    charge=(day*2)
    print("charge",charge)
elif day >6 and day <=10:
    charge=(day*3)-5
    print("charge",charge)
elif day >11 and day <15:
    charge=(day*4)-15
    print("charge",charge)
else:
    charge=(day*5)-30
    print("charge",charge)
