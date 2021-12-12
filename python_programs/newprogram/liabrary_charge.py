days = int(input("Eneter number of days you visit liabrary: "))
if days<=5:
    charge = days*2
    print("your library charge is", charge)
elif days>5 and days<=10:
    charge = 10+(days-5)*3
    print("Your library charge is", charge)
elif days>10 and days<=15:
    charge = 10+15+(days-10)*4
    print("Your library charge is", charge)
else:
    charge = 10+15+20+(days-15)*5
    print("Your liabrary charge is", charge)