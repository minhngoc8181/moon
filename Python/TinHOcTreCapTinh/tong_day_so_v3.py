K = int(input())
N = int(input())
numbers = []

for i in range(1, N + 1):
    numbers.extend([i] * K)
    if len(numbers) >= N:
        break

# print(numbers)
# print(numbers[:N])

print(sum(numbers[:N]))
