import hashlib

n = 10
# b turns into byte array
key = b"string"
# same as above
key2 = "string".encode()
key3 = b"lunchtime"


index = hash(key) % 8
index = hash(key2) % 8
index = hash(key3) % 8
print(index1)
print(index2)
print(index3)

# for i in range(n):
#     print(hash(key))
#     print(hashlib.sha256(key).hexdigest())
#
# for i in range(n):
#     print(hash(key)
#
# for i in range(n):
#     print(hash(key2)