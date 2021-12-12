price = int(input("calculate the net amount and discount"))
if price>10000:
    discount=price*20/100
    print("discount",discount)
elif price>7000 and price<=10000:
    discount=price*15/100
    print("discount", discount)
elif price<=7000:
    discount=price*10/100
    print("discount", discount)
else:
    print("invalid")        