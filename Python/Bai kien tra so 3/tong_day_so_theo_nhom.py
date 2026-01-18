N = int(input())
noItem = 0
total = 0
for i in range(1, N + 1):
    if noItem + i <= N:
        total += i * i
        noItem += i
    else:
        total += (N - noItem) * i
        break
print(total)