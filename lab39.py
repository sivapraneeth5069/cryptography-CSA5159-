from collections import Counter
english_freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
def score_text(text):
    text = ''.join(c for c in text if c.isalpha())
    freq = Counter(text)
    score = 0

    for i, ch in enumerate(english_freq):
        score += freq.get(ch, 0) * (26 - i)

    return score

def decrypt(ciphertext, key):
    plaintext = ""
    for ch in ciphertext:
        if ch.isalpha():
            p = (ord(ch) - ord('A') - key) % 26
            plaintext += chr(p + ord('A'))
        else:
            plaintext += ch

    return plaintext
ciphertext = input("Enter ciphertext: ").upper()
top_n = int(input("How many possible plaintexts to display? "))

results = []

for key in range(26):
    plain = decrypt(ciphertext, key)
    score = score_text(plain)
    results.append((score, key, plain))

results.sort(reverse=True)

print("\nTop Possible Plaintexts:\n")

for i in range(min(top_n, len(results))):
    score, key, plain = results[i]
    print(f"Guess {i+1}: Key = {key}, Plaintext = {plain}")