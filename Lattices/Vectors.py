import numpy as np

# Define the vectors
v = np.array([2, 6, 3])
w = np.array([1, 0, 0])
u = np.array([7, 7, 2])

# Calculate 2*v - w
result = 2 * v - w

# Calculate the inner product (dot product) of (2*v - w) and 2*u
inner_product = np.dot(result, 2 * u)

# Calculate the final result: 3 * inner_product
final_result = 3 * inner_product

print(f"The result of the calculation is {final_result}.")