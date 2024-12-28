p = 29
ints = [14, 6, 11]

def find_square_root_modulo(x, p):
    for a in range(p):
        if (a * a) % p == x:
            return a
    return None

for num in ints:
    root = find_square_root_modulo(num, p)
    if root is not None:
        print(f"The quadratic residue is {num}, its square root modulo {p} is {root}.")
        break
