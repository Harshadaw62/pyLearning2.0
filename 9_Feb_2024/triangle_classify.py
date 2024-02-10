"""Write a program that classifies a triangle based on its side lengths.
 Given three input values representing the lengths of the sides, determine
 if the triangle is equilateral (all sides are equal),
 isosceles (exactly two sides are equal), or scalene (no sides are equal)."""

side1 = int(input("Enter the length of Side1 of Triangle: "))
side2 = int(input("Enter the length of Side2 of Triangle: "))
side3 = int(input("Enter the length of Side3 of Triangle: "))
if side1 == side2 == side3:
    print("The Triangle is Equilateral")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("The Triangle is isosceles")
else:
    print("The Triangle is scalene")
