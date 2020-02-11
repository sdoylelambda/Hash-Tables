import hashlib

# b string - bytes string - strips away -- .encode() works too
key = b"str"
my_string = "normal string".encode()

# for i in range (10):
#     hashed = hashlib.sha256(key).hexdigest()
#     print(hashed)


for i in range(10):
    hashed = hash(key)
    print(hashed % 8)
