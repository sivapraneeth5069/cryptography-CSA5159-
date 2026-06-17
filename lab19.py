from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import base64

plaintext = input("Enter the plaintext: ")

key = DES3.adjust_key_parity(get_random_bytes(24))

iv = get_random_bytes(8)

cipher = DES3.new(key, DES3.MODE_CBC, iv)

ciphertext = cipher.encrypt(pad(plaintext.encode(), DES3.block_size))

print("\nKey (Base64):", base64.b64encode(key).decode())
print("IV (Base64):", base64.b64encode(iv).decode())
print("Ciphertext (Base64):", base64.b64encode(ciphertext).decode())