

q = int(input("Enter prime number q: "))
a = int(input("Enter primitive root a: "))

xA = int(input("Enter Alice's secret number: "))
xB = int(input("Enter Bob's secret number: "))

YA = pow(a, xA, q)   
YB = pow(a, xB, q)   

print("\nAlice sends:", YA)
print("Bob sends:", YB)

KA = pow(YB, xA, q)
KB = pow(YA, xB, q)

print("\nAlice's Shared Key:", KA)
print("Bob's Shared Key:", KB)