win = 5
i = 1
while i<5:
    num = int(input("Enter a number small and greater"))
    i = i+1
    if num != win:
        if num<win:
            print("small")
        else:
            print("greater")
    else:
        print("you win")
else:
    print("you loses")
    

