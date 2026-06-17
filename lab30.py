def xor(a, b):
    """XOR two binary strings"""
    result = ""
    for i in range(len(a)):
        result += str(int(a[i]) ^ int(b[i]))
    return result

def encrypt(block, key):
    return xor(block, key)
def cbc_mac(message, key):
    iv = "00000000"
    temp = xor(message, iv)
    tag = encrypt(temp, key)
    return tag

X = input("Enter 8-bit message block X: ")
K = input("Enter 8-bit secret key K: ")

T = cbc_mac(X, K)

print("\nMAC(K, X) =", T)

second_block = xor(X, T)

print("X XOR T =", second_block)

first = encrypt(X, K)
second = encrypt(xor(second_block, first), K)

print("MAC(K, X || (X XOR T)) =", second)