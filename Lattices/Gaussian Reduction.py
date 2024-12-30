import numpy as np

def gauss_lattice_reduction(v1, v2):
    while True:
        if np.linalg.norm(v2) < np.linalg.norm(v1):
            v1, v2 = v2, v1
        m = round(np.dot(v1, v2) / np.dot(v1, v1))
        if m == 0:
            return v1, v2
        v2 = v2 - m * v1

# Given vectors
v = np.array([846835985, 9834798552])
u = np.array([87502093, 123094980])

# Apply Gauss's algorithm
v1, v2 = gauss_lattice_reduction(v, u)

# Calculate the inner product of the new basis vectors
inner_product = np.dot(v1, v2)

print(f"The inner product of the new basis vectors is {inner_product}.")