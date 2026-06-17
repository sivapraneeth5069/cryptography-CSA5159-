def left_shift(binary):
    """Performs left shift by one bit"""
    return binary[1:] + "0"
def xor_binary(a, b):
    """XOR two binary strings"""
    result = ""
    for i in range(len(a)):
        result += str(int(a[i]) ^ int(b[i]))
    return result
block_size = int(input("Enter block size (64 or 128): "))

if block_size == 64:
    const = "00011011"    
elif block_size == 128:
    const = "10000111"    
else:
    print("Invalid block size!")
    exit()

L = input(f"Enter {block_size}-bit value L: ")

K1 = left_shift(L)
if L[0] == '1':
    K1 = K1[:-8] + xor_binary(K1[-8:], const)

K2 = left_shift(K1)
if K1[0] == '1':
    K2 = K2[:-8] + xor_binary(K2[-8:], const)

print("\nFirst Subkey (K1):")
print(K1)

print("\nSecond Subkey (K2):")
print(K2)