# Given integer
number = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

# Convert the integer to bytes
byte_data = number.to_bytes((number.bit_length() + 7) // 8, byteorder='big')

# Decode the bytes to a string (assuming ASCII encoding)
message = byte_data.decode('ascii')

print("The original message is:", message)
