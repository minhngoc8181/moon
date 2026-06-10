S = input()
ans = ''
number = 0
for c in S:
    if c in '01423456789':
        number = number * 10 + int(c)
    else:
        if c == 'A':
            ans += 'T' * number
        elif c == 'T':
            ans += 'A' * number
        elif c == 'G':
            ans += 'C' *  number
        else:
            ans += 'G' * number
        number = 0
print(ans)