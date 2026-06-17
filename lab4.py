from math import gcd
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None
def encrypt(text, a, b):
    cipher = ""
    for ch in text.upper():
        if ch.isalpha():
            p = ord(ch) - ord('A')
            c = (a * p + b) % 26
            cipher += chr(c + ord('A'))
        else:
            cipher += ch
    return cipher
def decrypt(cipher, a, b):
    plain = ""
    a_inv = mod_inverse(a, 26)
    for ch in cipher.upper():
        if ch.isalpha():
            c = ord(ch) - ord('A')
            p = (a_inv * (c - b)) % 26
            plain += chr(p + ord('A'))
        else:
            plain += ch
    return plain
text = input("Enter plaintext: ")
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
if gcd(a, 26) != 1:
    print("Invalid value of a!")
    print("For Affine Cipher, gcd(a,26) must be 1.")
else:
    cipher = encrypt(text, a, b)
    decrypted = decrypt(cipher, a, b)
    print("\nEncrypted Text :", cipher)
    print("Decrypted Text :", decrypted)