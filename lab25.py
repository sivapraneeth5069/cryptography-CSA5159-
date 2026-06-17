import math

n = int(input("Enter n (n = p * q): "))
m = int(input("Enter a plaintext block m: "))

g = math.gcd(m, n)

print("\ngcd(m, n) =", g)

if g > 1 and g < n:
    p = g
    q = n // g

    print("Common factor found!")
    print("p =", p)
    print("q =", q)
    print("RSA modulus n has been factored.")
else:
    print("No useful common factor found.")