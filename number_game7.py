win = 5
i = 1 
while i<=5:
    num = int(input("Enter a number between 1 to 10:"))
    i=i+1
    if num != win :
        print("plz try again")
    else:
        print("you win")
        break
else:
    print("yes loses")