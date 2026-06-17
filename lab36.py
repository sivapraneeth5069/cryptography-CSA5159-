def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

plaintext = input("Enter plaintext (A-Z only): ").upper()
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

if gcd(a, 26) != 1:
    print("\nEncryption is not possible.")
    print("For the affine cipher, gcd(a, 26) must be 1.")
else:
    ciphertext = ""

    for ch in plaintext:
        if 'A' <= ch <= 'Z':
            p = ord(ch) - ord('A')
            c = (a * p + b) % 26
            ciphertext += chr(c + ord('A'))
        else:
            ciphertext += ch

    print("\nCiphertext:", ciphertext)