N, K = map(int, input().split())
"""total = 0
count = 0
for i in range(1, N + 1):
    if count >= K:
        break
    if i % 2 == 0:
        total += i
        count += 1

for i in range(1, N + 1):
    if count >= K:
        break
    if i % 2 != 0 and i % 3 == 0:
        total += i
        count += 1

for i in range(1, N + 1):
    if count >= K:
        break
    if i % 2 != 0 and i % 3 != 0:
        total += i
        count += 1

print(total)"""

if K <= N // 2:
    print(sum(range(2, 2 * K, 2)))

