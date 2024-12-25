def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Test the function with given values
result = gcd(66528, 52920)
print("The GCD is:", result)
