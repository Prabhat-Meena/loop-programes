km=int(input("accept the kilomiter covered and calculate"))
if km<=10:
    bill=(km*11)
    print("bill",bill)
elif km>10 and km<90: 
    bill = 110+(km-10)*10
    print("bill",bill)
elif km>90:
    bill= 110+800+(km-100)*9
    print("bill",bill)

    
