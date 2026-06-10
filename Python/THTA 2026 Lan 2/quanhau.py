N = int(input())
x = int(input())
y = int(input())

total = 0
if (x + y) % 2 == 0:
    total = (
        min(x - 1, y - 1) + min(N - x, y - 1) + min(N - x, N - y) + min(x - 1, N - y)
    )

if x % 2 == 0:
    total += N // 2
else:
    total += (N + 1) // 2

if y % 2 == 0:
    total += N // 2
else:
    total += (N + 1) // 2

if (x + y) % 2 == 0:
    total -= 2

print(total)
