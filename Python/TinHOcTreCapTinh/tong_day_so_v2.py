K = int(input())
N = int(input())
numbers = []

for i in range(1, N + 1):
    for j in range(K):
        numbers.append(i)

# print(numbers)
# print(numbers[:N])
# print(sum(numbers[:N]))

total = 0
for i in range(N):
    total += numbers[i]

print(total)
