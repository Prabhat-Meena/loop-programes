day = int(input("Enter day number: "))
if (day>=1 and day<=7):
    if(day==1):
        print("Sunday")
    elif(day==2):
        print("Monday")
    elif(day==3):
        print("Tuesday")
    elif(day==4):
        print("Wednesday")
    elif(day==5):
        print("Thrusday")
    elif(day==6):
        print("Frieday")
    elif(day==7):
        print("Saturday")
else:
     print("invalid option")