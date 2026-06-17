shift_schedule = [1, 1, 2, 2, 2, 2, 2, 2,
                  1, 2, 2, 2, 2, 2, 2, 1]

def left_shift(bits, n):
    return bits[n:] + bits[:n]

def generate_subkeys(key):
    c = key[:28]   
    d = key[28:]   

    subkeys = []

    for i, shift in enumerate(shift_schedule):
        c = left_shift(c, shift)
        d = left_shift(d, shift)

        first_24 = c[:24]
        second_24 = d[:24]

        subkey = first_24 + second_24
        subkeys.append(subkey)

        print(f"K{i+1} = {subkey}")

    return subkeys


# Main Program
key = input("Enter a 56-bit binary key: ")

if len(key) != 56:
    print("Please enter exactly 56 bits.")
else:
    print("\nGenerated 48-bit DES Subkeys:\n")
    generate_subkeys(key)