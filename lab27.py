def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result
e = int(input("Enter public exponent (e): "))
n = int(input("Enter modulus (n): "))
message = input("Enter message (A-Z only): ").upper()

ciphertext = []

for ch in message:
    if 'A' <= ch <= 'Z':
        m = ord(ch) - ord('A')  
        c = mod_exp(m, e, n)
        ciphertext.append(c)

print("\nCiphertext Blocks:")
print(ciphertext)