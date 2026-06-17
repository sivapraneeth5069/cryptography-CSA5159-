from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
import base64
key = b'ABCDEFGH'
iv = b'12345678'  

plaintext = input("Enter the plaintext: ")

data = pad(plaintext.encode(), DES.block_size)

ecb = DES.new(key, DES.MODE_ECB)
ecb_cipher = ecb.encrypt(data)

cbc = DES.new(key, DES.MODE_CBC, iv)
cbc_cipher = cbc.encrypt(data)

cfb = DES.new(key, DES.MODE_CFB, iv)
cfb_cipher = cfb.encrypt(plaintext.encode())

print("\nECB Ciphertext:")
print(base64.b64encode(ecb_cipher).decode())

print("\nCBC Ciphertext:")
print(base64.b64encode(cbc_cipher).decode())

print("\nCFB Ciphertext:")
print(base64.b64encode(cfb_cipher).decode())