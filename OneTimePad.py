import binascii
import os
import sys

def hex_strxor(a, b):     # xor two strings of different lengths
    res = [x ^ y for (x, y) in zip(binascii.unhexlify(a), binascii.unhexlify(b))]
    return bytes(res).hex()

def encode_hex(s):
    return s.encode('utf-8').hex()

def decode_hex(s):
    return bytes.fromhex(s).decode('utf-8')

def main():
    m1 = encode_hex("hello world!")
    key = os.urandom(12).hex()
    c1 = hex_strxor(m1, key)
    print(c1)
    
if __name__ == '__main__':
    main()