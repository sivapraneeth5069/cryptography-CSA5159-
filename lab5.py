from math import gcd
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None
def decrypt(ciphertext, a, b):
    plaintext = ""
    a_inv = mod_inverse(a, 26)
    for ch in ciphertext.upper():
        if ch.isalpha():
            c = ord(ch) - ord('A')
            p = (a_inv * (c - b)) % 26
            plaintext += chr(p + ord('A'))
        else:
            plaintext += ch
    return plaintext
ciphertext = input("Enter ciphertext: ")
print("\nPossible Plaintexts:\n")
for a in range(1, 26):
    if gcd(a, 26) == 1:  
        for b in range(26):
            plaintext = decrypt(ciphertext, a, b)
            print(f"a={a:2}, b={b:2} --> {plaintext}")