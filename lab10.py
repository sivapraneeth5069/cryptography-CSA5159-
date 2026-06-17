matrix = [
['M','F','H','I','K'],
['U','N','O','P','Q'],
['Z','V','W','X','Y'],
['E','L','A','R','G'],
['D','S','T','B','C']
]
def pos(ch):
    if ch == 'J': ch = 'I'
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j
msg = input("Enter Message: ").upper().replace(" ","").replace(".","")
pairs = []
i = 0
while i < len(msg):
    a = msg[i]
    b = msg[i+1] if i+1 < len(msg) else 'X'
    if a == b:
        pairs.append(a+'X')
        i += 1
    else:
        pairs.append(a+b)
        i += 2
cipher = ""
for p in pairs:
    a, b = p[0], p[1]
    r1, c1 = pos(a)
    r2, c2 = pos(b)

    if r1 == r2:
        cipher += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
    elif c1 == c2:
        cipher += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
    else:
        cipher += matrix[r1][c2] + matrix[r2][c1]
print("Cipher Text:", cipher)