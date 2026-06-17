import math

def gcd_extended(a, b):
    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = gcd_extended(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def mod_inverse(e, phi):
    gcd, x, y = gcd_extended(e, phi)
    if gcd != 1:
        return None
    return x % phi

p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))
e = int(input("Enter public exponent e: "))

n = p * q
phi = (p - 1) * (q - 1)

d = mod_inverse(e, phi)

print("\nPublic Key  : (e, n) =", (e, n))
print("Private Key : (d, n) =", (d, n))