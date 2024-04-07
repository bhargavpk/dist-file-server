'''
Contains utilitary functions for hashing
'''

from hashlib import sha256

def hashStrToSha256(key):
    key_hash = sha256(key.encode('utf-8')).hexdigest()
    return key_hash

# Supports only text files for now
def hashFile(path):
    f = open(path, 'r')
    content = f.read()
    f.close()
    return hashStrToSha256(content)

# Hash string to a number from 0 to 255
def hashStrToNum(str):
    # Prime number for hashing
    p = 307
    m = 256
    hash_val = 0
    for i in range(len(str)):
        hash_val = (hash_val + ord(str[i])*(p**i))%m
    return hash_val


name = 'bpa'
print(hashStrToNum(name))


