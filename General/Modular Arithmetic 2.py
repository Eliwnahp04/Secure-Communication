# Fermat's Little Theorem Calculations

# Step 1: 3^17 mod 17
result_3 = pow(3, 17, 17)

# Step 2: 5^17 mod 17
result_5 = pow(5, 17, 17)

# Step 3: 7^16 mod 17
result_7 = pow(7, 16, 17)

# Step 4: 273246787654^65536 mod 65537
result_large = pow(273246787654, 65536, 65537)

# Print results
print(f"3^17 mod 17 = {result_3}")
print(f"5^17 mod 17 = {result_5}")
print(f"7^16 mod 17 = {result_7}")
print(f"273246787654^65536 mod 65537 = {result_large}")
