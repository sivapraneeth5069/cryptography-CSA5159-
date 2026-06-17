alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
keyword = input("Enter Keyword: ").upper()
plaintext = input("Enter Plaintext: ").upper()
cipher_alphabet = ""
for ch in keyword:
    if ch not in cipher_alphabet:
        cipher_alphabet += ch
for ch in alphabet:
    if ch not in cipher_alphabet:
        cipher_alphabet += ch
print("Plain Alphabet :", alphabet)
print("Cipher Alphabet:", cipher_alphabet)
ciphertext = ""
for ch in plaintext:
    if ch.isalpha():
        index = alphabet.index(ch)
        ciphertext += cipher_alphabet[index]
    else:
        ciphertext += ch
print("Encrypted Text :", ciphertext)
decrypted = ""
for ch in ciphertext:
    if ch.isalpha():
        index = cipher_alphabet.index(ch)
        decrypted += alphabet[index]
    else:
        decrypted += ch
print("Decrypted Text :", decrypted)