from collections import Counter
english_freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def frequency_attack(ciphertext, top_n):
    ciphertext = ciphertext.upper()

    letters = [ch for ch in ciphertext if ch.isalpha()]
    freq = Counter(letters)

    cipher_freq = ''.join([item[0] for item in freq.most_common()])

    print("\nTop", top_n, "Possible Plaintexts:\n")

    for k in range(top_n):
        mapping = {}
        shifted = english_freq[k:] + english_freq[:k]

        for i in range(min(len(cipher_freq), len(shifted))):
            mapping[cipher_freq[i]] = shifted[i]

        # Decrypt text
        plaintext = ""
        for ch in ciphertext:
            if ch.isalpha():
                plaintext += mapping.get(ch, ch)
            else:
                plaintext += ch

        print(f"Possibility {k+1}: {plaintext}")


# Main Program
cipher = input("Enter the ciphertext: ")
n = int(input("Enter number of possible plaintexts to display: "))
frequency_attack(cipher, n)