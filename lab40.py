from collections import Counter
english_freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

ciphertext = input("Enter ciphertext: ").upper()
top_n = int(input("Enter number of possible plaintexts: "))
letters = [ch for ch in ciphertext if ch.isalpha()]
freq = Counter(letters)
cipher_order = ''.join([x[0] for x in freq.most_common()])

results = []
for shift in range(top_n):
    mapping = {}
    rotated = english_freq[shift:] + english_freq[:shift]
    for i in range(min(len(cipher_order), 26)):
        mapping[cipher_order[i]] = rotated[i]
    plaintext = ""
    for ch in ciphertext:
        if ch.isalpha():
            plaintext += mapping.get(ch, ch)
        else:
            plaintext += ch
    results.append(plaintext)
print("\nTop Possible Plaintexts:\n")
for i, text in enumerate(results, start=1):
    print(f"Guess {i}: {text}")