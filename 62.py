# Write a Python program to calculate surface volume and area of acylinder 

pi = 3.14159
radius = float(input("enter radius :-"))
height = float(input("enter height :-"))
volume = pi * radius**2 * height
surface_area = 2 * pi * radius * (radius + height)
# print(f"Volume of the cylinder: {volume:.2f}")
# print(f"Surface area of the cylinder: {surface_area:.2f}")
print(volume)
print(surface_area)