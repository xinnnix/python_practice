import hashlib, binascii
sha3_256hash = hashlib.sha3_256(b'hello world').digest()
print("SHA3-256('hello world') =", binascii.hexlify(sha3_256hash))
