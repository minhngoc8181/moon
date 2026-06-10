M = int(input())
total = 0
for i in range(1, M + 2):
    total += i
    if total > M:
        print(i)
        break