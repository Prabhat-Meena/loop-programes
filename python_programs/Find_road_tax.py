costPrice = int(input("Enter a number"))
if costPrice<=50000:
    tax = costPrice*5/100
    print("Your road tax is",tax)
elif(costPrice>50000 and costPrice<=100000):
    tax = costPrice*10/100
    print("Your road tax is", tax)
elif(costPrice>100000):
    tax = costPrice*15/100
    print("Your road tax is", tax)
