list1 = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "Octomber", "November", "December" ]
month = input("enter")
print(list1[2])
if (month==list1[0] or month==list1[2] or month== list1[4] or month== list1[6] or month== list1[7] or month==list1[9] or month==list1[11]):
    print("31 days in", month)
elif month==list1[1]:
    print("28/29 days in", month)
else:
    print("30 days in", month)