side1 = 5   # replace with your values
side2 = 4
side3 = 4

if side1 == side2 and side2 == side3:
    print("Equilateral triangle")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
