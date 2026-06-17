shift_schedule = [1, 1, 2, 2, 2, 2, 2, 2,
                  1, 2, 2, 2, 2, 2, 2, 1]

def left_shift(bits, n):
    return bits[n:] + bits[:n]

def generate_keys(key):
    c = key[:28]
    d = key[28:]
    keys = []

    for shift in shift_schedule:
        c = left_shift(c, shift)
        d = left_shift(d, shift)
        round_key = c + d
        keys.append(round_key)

    return keys

# Main Program
key = input("Enter a 56-bit binary key: ")

if len(key) != 56:
    print("Please enter exactly 56 bits.")
else:
    encryption_keys = generate_keys(key)
    decryption_keys = encryption_keys[::-1]

    print("\nEncryption Keys:")
    for i, k in enumerate(encryption_keys, start=1):
        print(f"K{i} = {k}")

    print("\nDecryption Keys (Reverse Order):")
    for i, k in enumerate(decryption_keys, start=1):
        print(f"K{i} = {k}")