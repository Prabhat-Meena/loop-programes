
side1 = int(input("Ener first side of triangle: "))
side2 = int(input("Enter second side of triangle: "))
side3 = int(input("Enter third side of triangle: "))
if (side1==side2 and side1==side3):
    print("Equilateral Trianglle")
elif (side1!=side2 and side1!=side3):
    print("Scalene Triangle")
else:
    print("Isosceles Triangle")