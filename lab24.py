def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y
def mod_inverse(e, phi):
    gcd, x, y = extended_gcd(e, phi)

    if gcd != 1:
        return None
    else:
        return x % phi
e = int(input("Enter public exponent (e): "))
n = int(input("Enter modulus (n): "))

p = q = None
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        p = i
        q = n // i
        break
print("\nPrime factors:")
print("p =", p)
print("q =", q)

phi = (p - 1) * (q - 1)
print("phi(n) =", phi)

d = mod_inverse(e, phi)

print("\nPrivate Key:")
print("(d, n) = ({}, {})".format(d, n))