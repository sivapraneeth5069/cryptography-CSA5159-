def xor(a, b):
    """XOR two binary strings"""
    result = ""
    for i in range(len(a)):
        result += str(int(a[i]) ^ int(b[i]))
    return result
def sdes_encrypt(block, key):
    key8 = key[:8]       
    return xor(block, key8)


def sdes_decrypt(block, key):
    key8 = key[:8]
    return xor(block, key8)


def cbc_encrypt(plaintext, key, iv):
    ciphertext = ""
    previous = iv

    for i in range(0, len(plaintext), 8):
        block = plaintext[i:i+8]

        temp = xor(block, previous)

        cipher_block = sdes_encrypt(temp, key)

        ciphertext += cipher_block
        previous = cipher_block

    return ciphertext
def cbc_decrypt(ciphertext, key, iv):
    plaintext = ""
    previous = iv

    for i in range(0, len(ciphertext), 8):
        block = ciphertext[i:i+8]

        temp = sdes_decrypt(block, key)

        plain_block = xor(temp, previous)

        plaintext += plain_block
        previous = block

    return plaintext


# Main Program
plaintext = input("Enter 16-bit binary plaintext: ")
key = input("Enter 10-bit binary key: ")
iv = input("Enter 8-bit binary IV: ")

ciphertext = cbc_encrypt(plaintext, key, iv)
print("\nCiphertext :", ciphertext)

decrypted = cbc_decrypt(ciphertext, key, iv)
print("Decrypted Text :", decrypted)