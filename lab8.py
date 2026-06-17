plain_alphabet = "abcdefghijklmnopqrstuvwxyz"
cipher_alphabet = "cipherabdfgjklmnoqstuvwxyz"
def encrypt(text):
    result = ""
    for ch in text.lower():
        if ch in plain_alphabet:
            index = plain_alphabet.index(ch)
            result += cipher_alphabet[index]
        else:
            result += ch
    return result
def decrypt(text):
    result = ""
    for ch in text.lower():
        if ch in cipher_alphabet:
            index = cipher_alphabet.index(ch)
            result += plain_alphabet[index]
        else:
            result += ch
    return result
choice = input("Enter E for Encryption or D for Decryption: ").upper()

if choice == 'E':
    plaintext = input("Enter Plain Text: ")
    ciphertext = encrypt(plaintext)
    print("Cipher Text:", ciphertext)

elif choice == 'D':
    ciphertext = input("Enter Cipher Text: ")
    plaintext = decrypt(ciphertext)
    print("Plain Text:", plaintext)

else:
    print("Invalid Choice!")