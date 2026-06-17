from collections import Counter
ciphertext = input("Enter Cipher Text:\n")
freq = Counter(ciphertext)
print("\nCharacter Frequency Analysis:")
for char, count in freq.most_common():
    print(f"{char} : {count}")
english_freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
print("\nMost Common Characters in Ciphertext:")
cipher_chars = [char for char, count in freq.most_common()]
for i in range(min(len(cipher_chars), len(english_freq))):
    print(cipher_chars[i], "->", english_freq[i])
print("\nPossible Substitution Mapping Generated.")
print("Use the mapping and common words such as 'THE', 'AND', 'THAT'")
print("to complete the decryption manually.")