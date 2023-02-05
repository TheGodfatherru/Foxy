from hashlib import md5

print(md5('046d:c31c'.encode()).hexdigest())
print(md5('046d:c05a'.encode()).hexdigest())