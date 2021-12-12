marketPrice = int(input("Enter the market price of goods: "))
if marketPrice<=7000:
    discount = marketPrice*10/100
    netAmount = marketPrice-discount
    print("Net amount to pay is", netAmount)
elif marketPrice>7000 and marketPrice<=10000:
    discount = marketPrice*15/100
    netAmount = marketPrice-discount
    print(" net amount to pay is", netAmount)
else:
    discount= marketPrice*20/100
    netAmount = marketPrice-discount
    print("net amount to be pay is", netAmount)