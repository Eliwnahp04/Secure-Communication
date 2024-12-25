from binascii import unhexlify

ciphertext_hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
ciphertext = unhexlify(ciphertext_hex)

def xor_with_key(data, key):
    return bytes(byte ^ key for byte in data)

for key in range(256):
    plaintext = xor_with_key(ciphertext, key)
    try:
        decoded = plaintext.decode('utf-8')
        if all(32 <= ord(c) <= 126 for c in decoded):
            print(f"Key: {key}, Message: {decoded}")
    except UnicodeDecodeError:
        continue
