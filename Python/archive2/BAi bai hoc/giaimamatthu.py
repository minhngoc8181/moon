S = input()
letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(0, len(S), 2):
    c = S[i]
    d = int(S[i + 1])
    pos = letter.index(c)
    newc = letter[pos + d]
    print(newc, end = '')