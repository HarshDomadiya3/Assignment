# Write a Python program to calculate the area of a trapezoid 

# def trapezoid_area(base1, base2, height):
#     return 0.5 * (base1 + base2) * height
# base1 = 5  
# base2 = 7  
# height = 4  
# area = trapezoid_area(base1, base2, height)
# print(f"The area of the trapezoid is {area}")

b1 = float(input("Enter the length of the first base of the trapezoid: "))
b2 = float(input("Enter the length of the second base of the trapezoid: "))
height = float(input("Enter the height of the trapezoid: "))

# Calculate area
area = 0.5 * (b1 + b2) * height

# Output the result
print(f"The area of the trapezoid is: {area}")