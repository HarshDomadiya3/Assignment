# Write a Python program to read a random line from a file. 

import random

# Open the file
file = open('yourfile')

# Read all lines
lines = file.readlines()

# Close the file
file.close()

# Print a random line
print(random.choice(lines))