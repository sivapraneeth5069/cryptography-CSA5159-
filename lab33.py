
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64

plaintext = input("Enter plaintext: ")
key = b'ABCDEFGH'

cipher = DES.new(key, DES.MODE_ECB)

ciphertext = cipher.encrypt(pad(plaintext.encode(), DES.block_size))

decrypted = unpad(cipher.decrypt(ciphertext), DES.block_size)

print("\nPlaintext :", plaintext)
print("Ciphertext (Base64) :", base64.b64encode(ciphertext).decode())
print("Decrypted Text :", decrypted.decode())