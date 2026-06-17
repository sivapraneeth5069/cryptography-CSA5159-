from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
import base64
key = b'ABCDEFGH'

plaintext = input("Enter the plaintext: ")

cipher = DES.new(key, DES.MODE_ECB)

ciphertext = cipher.encrypt(pad(plaintext.encode(), DES.block_size))

print("\nCiphertext (Base64):")
print(base64.b64encode(ciphertext).decode())