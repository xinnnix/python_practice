import hashlib, binascii

sha256hash = hashlib.sha256(b'hello world').digest()
print("SHA-256('hello world') = ", binascii.hexlify(sha256hash))
