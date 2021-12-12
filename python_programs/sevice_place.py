employee_age = int(input("Enter your age: "))
employee_gender = input(" Enter your gender 'M or F': ")
marital_status = input("Enter 'Y' if you are merried or enter 'N' if you are not merried: ")
if(employee_age<20 or employee_age>60):
    print("ERROR")
elif(employee_gender=='F'):
    print("you will work only in urban areas")
elif(employee_gender=='M'):
    if(employee_age>=40 and employee_age<=60):
        print("you will work in urban area only")
    else:
        print("you may work anywhere")