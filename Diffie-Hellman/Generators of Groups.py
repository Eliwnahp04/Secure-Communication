def is_primitive_root(g, p):
    # Check if g is a primitive root of the finite field F_p
    required_set = set(num for num in range(1, p))
    actual_set = set(pow(g, powers, p) for powers in range(1, p))
    return required_set == actual_set

def find_smallest_primitive_root(p):
    for g in range(2, p):
        if is_primitive_root(g, p):
            return g
    return None

# Given prime p
p = 28151

# Find the smallest primitive element g
smallest_primitive_root = find_smallest_primitive_root(p)

print(f"The smallest primitive element g of the finite field F_{p} is {smallest_primitive_root}.")