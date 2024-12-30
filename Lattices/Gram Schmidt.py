import numpy as np

def gram_schmidt(vectors):
    basis = []
    for v in vectors:
        w = v.copy()
        for b in basis:
            w -= np.dot(v, b) / np.dot(b, b) * b
        basis.append(w)
    return np.array(basis)

# Given basis vectors
v1 = np.array([4, 1, 3, -1])
v2 = np.array([2, 1, -3, 4])
v3 = np.array([1, 0, -2, 7])
v4 = np.array([6, 2, 9, -5])

# Apply Gram-Schmidt algorithm
orthogonal_basis = gram_schmidt([v1, v2, v3, v4])

# Get the second component of u4
u4_second_component = orthogonal_basis[3][1]

# Print the result to 5 significant figures
print(f"The second component of u4 to 5 significant figures is {u4_second_component:.5g}.")