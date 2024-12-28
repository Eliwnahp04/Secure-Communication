def mod_inverse(a, p):
    # Using Extended Euclidean Algorithm to find the modular inverse
    m0, x0, x1 = p, 0, 1
    if p == 1:
        return 0
    while a > 1:
        # q is quotient
        q = a // p
        t = p
        # m is remainder now, process same as Euclid's algo
        p = a % p
        a = t
        t = x0
        x0 = x1 - q * x0
        x1 = t
    # Make x1 positive
    if x1 < 0:
        x1 += m0
    return x1

# Given values
p = 991
g = 209

# Calculate the inverse element d such that (g * d) % p == 1
d = mod_inverse(g, p)

print(f"The inverse element d such that (g * d) % {p} == 1 is {d}.")