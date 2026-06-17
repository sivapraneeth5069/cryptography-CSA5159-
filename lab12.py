key = [[9, 4],
       [5, 7]]
text = input("Enter Plain Text: ").lower().replace(" ", "")
if len(text) % 2 != 0:
    text += 'x'
cipher = ""
for i in range(0, len(text), 2):
    p1 = ord(text[i]) - 97
    p2 = ord(text[i+1]) - 97
    c1 = (9*p1 + 4*p2) % 26
    c2 = (5*p1 + 7*p2) % 26
    cipher += chr(c1 + 97) + chr(c2 + 97)
print("Cipher Text:", cipher)
inverse = [[5,22],
           [23,9]]
plain = ""
for i in range(0, len(cipher), 2):
    c1 = ord(cipher[i]) - 97
    c2 = ord(cipher[i+1]) - 97
    p1 = (5*c1 + 22*c2) % 26
    p2 = (23*c1 + 9*c2) % 26
    plain += chr(p1 + 97) + chr(p2 + 97)
print("Decrypted Text:", plain)