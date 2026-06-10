S = input()
K = int(input())
letters = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
for l in S:
    index = letters.index(l)
    newletter = letters[index + K]
    print(newletter, end = '')


"""c = S[l]
d = int(S[l + 1])
pos = letter.index(c)
newc = letter[pos + d]
print(newc, end = '')"""