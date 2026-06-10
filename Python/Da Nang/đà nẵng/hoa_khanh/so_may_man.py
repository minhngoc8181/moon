N = input()
total = 0
for d in N:
    i = int(d)
    if i != 4 or i != 8:
        solon = max(4, 8, i)
        sobe = min(4, 8, i)
        if i == solon:
            total += i  - 8
        elif i == sobe:
            total += 4 - i
        else:
            total += min(8 - i, i - 4)
print(total)