text = input("Enter the plaintext: ")
k = int(input("Enter the key value (1-25): "))
ciphertext = ""
for char in text:
    if char.isalpha():
        if char.islower():
            ciphertext += chr((ord(char) - ord('a') + k) % 26 + ord('a'))
        else:
            ciphertext += chr((ord(char) - ord('A') + k) % 26 + ord('A'))
    else:
        ciphertext += char
print("Encrypted Text:", ciphertext)
decrypted_text = ""
for char in ciphertext:
    if char.isalpha():
        if char.islower():
            decrypted_text += chr((ord(char) - ord('a') - k) % 26 + ord('a'))
        else:
            decrypted_text += chr((ord(char) - ord('A') - k) % 26 + ord('A'))
    else:
        decrypted_text += char
print("Decrypted Text:", decrypted_text)