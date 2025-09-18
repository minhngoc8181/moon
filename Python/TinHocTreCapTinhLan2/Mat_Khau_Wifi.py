K = int(input())
numbers = []
for i in range(2, K + 5, 2):
    numbers.extend([i] * (i - 1))
    if len(numbers) >= K:
        break
print(numbers[K - 1])
