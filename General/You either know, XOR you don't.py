from itertools import cycle

ciphertext = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
known_plaintext = "crypto{"[:7]

key_part = bytes(a ^ b for a, b in zip(ciphertext, known_plaintext.encode()))
key = (key_part + b'y').decode()  # Extend the key based on observation

plaintext = bytes(c ^ k for c, k in zip(ciphertext, cycle(key.encode()))).decode()

print(plaintext)
