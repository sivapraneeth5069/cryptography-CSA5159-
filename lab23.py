def xor(a, b):
    """XOR two binary strings"""
    result = ""
    for i in range(len(a)):
        result += str(int(a[i]) ^ int(b[i]))
    return result

def sdes_encrypt(counter, key):
    key8 = key[:8] 
    return xor(counter, key8)
def ctr_mode(data, key):
    result = ""
    counter = 0
    for i in range(0, len(data), 8):
        block = data[i:i + 8]

        counter_bin = format(counter, '08b')

        keystream = sdes_encrypt(counter_bin, key)

        result += xor(block, keystream)

        counter += 1

    return result
plaintext = input("Enter binary plaintext: ")
key = input("Enter 10-bit binary key: ")

ciphertext = ctr_mode(plaintext, key)
print("\nCiphertext :", ciphertext)

decrypted = ctr_mode(ciphertext, key)
print("Decrypted Text :", decrypted)