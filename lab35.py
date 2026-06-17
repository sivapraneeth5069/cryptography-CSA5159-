
plaintext = input("Enter plaintext (A-Z only): ").upper()

key = list(map(int, input(
    "Enter key values separated by spaces: ").split()))

if len(key) != len(plaintext):
    print("Error: Number of key values must equal the plaintext length.")
else:
    ciphertext = ""

    for i in range(len(plaintext)):
        if 'A' <= plaintext[i] <= 'Z':
            p = ord(plaintext[i]) - ord('A')
            c = (p + key[i]) % 26
            ciphertext += chr(c + ord('A'))
        else:
            ciphertext += plaintext[i]

    print("\nCiphertext:", ciphertext)