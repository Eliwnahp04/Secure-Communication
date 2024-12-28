from sympy import isprime

# Given integers
integers = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]

# Function to find the prime p and integer x
def find_p_and_x(integers):
    for p in range(100, 1000):
        if isprime(p):
            for x in range(2, p):
                valid = True
                for i in range(len(integers)):
                    if pow(x, i + 1, p) != integers[i]:
                        valid = False
                        break
                if valid:
                    return p, x
    return None, None

# Find p and x
p, x = find_p_and_x(integers)

if p and x:
    print(f"The prime p is: {p}")
    print(f"The integer x is: {x}")
else:
    print("No valid p and x found.")