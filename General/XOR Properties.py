from binascii import unhexlify

key1 = unhexlify("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
key2_xor_key1 = unhexlify("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
key2_xor_key3 = unhexlify("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
flag_xor_keys = unhexlify("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

key2 = bytes(a ^ b for a, b in zip(key1, key2_xor_key1))
key3 = bytes(a ^ b for a, b in zip(key2, key2_xor_key3))
flag = bytes(a ^ b ^ c ^ d for a, b, c, d in zip(flag_xor_keys, key1, key2, key3))

print("The flag is:", flag.decode('utf-8'))
