import math

# Define the vector
v = [4, 6, 2, 5]

# Calculate the size of the vector
size = math.sqrt(sum([x**2 for x in v]))

print(f"The size of the vector v is {size}.")