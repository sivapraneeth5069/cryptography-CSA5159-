def pos(m, ch):
    if ch == 'J': ch = 'I'
    for i in range(5):
        for j in range(5):
            if m[i][j] == ch:
                return i, j
key = input("Enter Key: ").upper().replace(" ", "")
s = ""
for c in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
    if c not in s:
        s += c
m = [list(s[i:i+5]) for i in range(0, 25, 5)]
ct = input("Enter Cipher Text: ").upper().replace(" ", "")
pt = ""
for i in range(0, len(ct), 2):
    a, b = ct[i], ct[i+1]
    r1, c1 = pos(m, a)
    r2, c2 = pos(m, b)
    if r1 == r2:
        pt += m[r1][(c1-1)%5] + m[r2][(c2-1)%5]
    elif c1 == c2:
        pt += m[(r1-1)%5][c1] + m[(r2-1)%5][c2]
    else:
        pt += m[r1][c2] + m[r2][c1]
print("Plain Text:", pt)