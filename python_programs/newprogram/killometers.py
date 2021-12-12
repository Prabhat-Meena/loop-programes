kilo = int(input("Enter a num"))
if kilo<=10:
    charge = kilo*11
    print("Your bus charge is", charge)
elif(kilo>10 and kilo<=90):
    charge = 110+(kilo-10)*10
    print("Your bus charge is", charge)
elif(kilo>90):
    charge = 110+800+(kilo-90)*9
    print("Your bus charge is", charge)
