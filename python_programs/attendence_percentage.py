classes_held = int(input("Enter number of classes held: "))
classes_attended = int(input("Enter number of classes attended"))
medical_cause = input("Enter 'y or n': ")
attendence = classes_held*75/100
if (classes_attended<attendence):
    if(medical_cause=='y'):
        print("This student is allowed")
    else:
        print("This student is not allowed to sit in exam")
else:
    print("This student is allowed to sit in exam")