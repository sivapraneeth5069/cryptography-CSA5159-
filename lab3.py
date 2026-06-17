plain_alphabet = "abcdefghijklmnopqrstuvwxyz"
cipher_alphabet = "qwertyuiopasdfghjklzxcvbnm"

encrypt_dict = dict(zip(plain_alphabet, cipher_alphabet))
decrypt_dict = dict(zip(cipher_alphabet, plain_alphabet))

plaintext = input("Enter the plaintext: ").lower()

ciphertext = ""
for char in plaintext:
    if char.isalpha():
        ciphertext += encrypt_dict[char]
    else:
        ciphertext += char

print("Encrypted Text:", ciphertext)

decrypted_text = ""
for char in ciphertext:
    if char.isalpha():
        decrypted_text += decrypt_dict[char]
    else:
        decrypted_text += char

print("Decrypted Text:", decrypted_text)