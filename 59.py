# Write a Python program to convert degree to radian


# import math
# def degrees_to_radians(degrees):
#     return degrees * (math.pi / 180)
# degrees = 45  
# radians = degrees_to_radians(degrees)
# print(f"{degrees} degrees is equal to {radians} radians")

pi = 3.141592653589793

# Input from user
degrees = float(input("Enter the angle in degrees: "))

# Convert degrees to radians
radians = degrees * (pi / 180)

# Output the result
print(radians)