def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, u1, v1 = extended_gcd(b, a % b)
    u = v1
    v = u1 - (a // b) * v1
    return g, u, v

p = 26513
q = 32321

gcd, u, v = extended_gcd(p, q)

# Since gcd(p, q) = 1, we know the result will be u and v such that p * u + q * v = 1
print(f"u: {u}, v: {v}")
