
from collections import Counter

english_freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

ciphertext = input("Enter ciphertext: ").upper()
top_n = int(input("How many possible plaintexts to display? "))

letters = [c for c in ciphertext if c.isalpha()]
freq = Counter(letters)

cipher_order = ''.join(
    [item[0] for item in freq.most_common()]
)
print("\nPossible Plaintexts:\n")

for k in range(top_n):
    mapping = {}
    rotated = english_freq[k:] + english_freq[:k]

    for i in range(min(len(cipher_order), 26)):
        mapping[cipher_order[i]] = rotated[i]

    plaintext = ""
    for ch in ciphertext:
        if ch.isalpha():
            plaintext += mapping.get(ch, ch)
        else:
            plaintext += ch

    print(f"Guess {k + 1}: {plaintext}")