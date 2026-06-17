cipher = input("Enter Cipher Text: ").lower()
n = int(input("Enter number of possible plaintexts: "))
for key in range(n):
    plain = ""
    for ch in cipher:
        if ch.isalpha():
            plain += chr((ord(ch) - ord('a') - key) % 26 + ord('a'))
        else:
            plain += ch
    print("Key", key, ":", plain)