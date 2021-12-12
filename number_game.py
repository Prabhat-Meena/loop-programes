jackpot = 5
i = 1
while(i<=5):
    a = int(input("guess a number between 1 to 10: "))
    i = i+1
    if a != jackpot:
        if(a<jackpot):
            print("Number entered by you enterd is small, try one more time")
        else:
            print("Number entered by you enterd is greater, try one more time")
    else:
         print("you win")
         break
else:
    print("you loses") 


