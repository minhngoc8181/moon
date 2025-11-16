M = int(input())
N = int(input())
count = 0
for i in range(M):
    start = N * i + 1
    for j in range(start, start + N):
        if j % 5 == 0:
            count += j - start + 1
            count += i
            count %= 2025
print(count)
