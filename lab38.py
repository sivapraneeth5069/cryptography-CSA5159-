def hill_encrypt(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "")
    if len(plaintext) % 2 != 0:
        plaintext += 'X'

    ciphertext = ""

    for i in range(0, len(plaintext), 2):
        p1 = ord(plaintext[i]) - ord('A')
        p2 = ord(plaintext[i + 1]) - ord('A')
        c1 = (key[0][0] * p1 + key[0][1] * p2) % 26
        c2 = (key[1][0] * p1 + key[1][1] * p2) % 26

        ciphertext += chr(c1 + ord('A'))
        ciphertext += chr(c2 + ord('A'))

    return ciphertext
plaintext = input("Enter plaintext: ")

print("Enter 2 × 2 key matrix:")
a = int(input("a11 = "))
b = int(input("a12 = "))
c = int(input("a21 = "))
d = int(input("a22 = "))

key = [[a, b],
       [c, d]]

ciphertext = hill_encrypt(plaintext, key)

print("\nPlaintext :", plaintext.upper())
print("Ciphertext:", ciphertext)