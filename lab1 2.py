from collections import Counter
import string
plain_alphabets = "abcdefghijklmnopqrstuvwxyz"
cipher_alphabets = "QWERTYUIOPASDFGHJKLZXCVBNM".lower()

encrypt_dict = dict(zip(plain_alphabets, cipher_alphabets))
decrypt_dict = dict(zip(cipher_alphabets, plain_alphabets))


with open("plaintext.txt", "r") as file:
    plaintext = file.read().lower()
ciphertext = ''.join(encrypt_dict.get(ch, ch) for ch in plaintext)

with open("ciphertext.txt", "w") as file:
    file.write(ciphertext)

decrypted_text = ''.join(decrypt_dict.get(ch, ch) for ch in ciphertext)


plain_freq = Counter(plaintext)
cipher_freq = Counter(ciphertext)

print("\nFrequency Analysis")
print("-" * 40)
print("Alphabet\tPlaintext\tCiphertext")
print("-" * 40)

for ch in string.ascii_lowercase:
    print(f"{ch}\t\t{plain_freq[ch]}\t\t{cipher_freq[ch]}")

print("\nEncryption completed successfully.")
print("Ciphertext stored in ciphertext.txt")

print("\nFirst 100 characters of Plaintext:")
print(plaintext[:100])

print("\nFirst 100 characters of Ciphertext:")
print(ciphertext[:100])

print("\nFirst 100 characters after Decryption:")
print(decrypted_text[:100])