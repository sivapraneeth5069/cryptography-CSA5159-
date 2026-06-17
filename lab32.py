import random
import hashlib
message = input("Enter a message: ")

h = int(hashlib.sha256(message.encode()).hexdigest(), 16)
d = 7
n = 33
rsa_sig1 = pow(h, d, n)
rsa_sig2 = pow(h, d, n)

print("\nRSA Signatures:")
print("Signature 1:", rsa_sig1)
print("Signature 2:", rsa_sig2)

if rsa_sig1 == rsa_sig2:
    print("Both signatures are identical.")

q = 101

k1 = random.randint(1, q - 1)
k2 = random.randint(1, q - 1)

dsa_sig1 = (h + k1) % q
dsa_sig2 = (h + k2) % q

print("\nDSA Signatures:")
print("Signature 1:", dsa_sig1)
print("Signature 2:", dsa_sig2)

if dsa_sig1 != dsa_sig2:
    print("Signatures are different because k is random.")