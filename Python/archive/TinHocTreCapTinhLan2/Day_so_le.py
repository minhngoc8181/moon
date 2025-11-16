N = int(input())
K = int(input())
numbers = []
for i in range(2, N + 1, 2):
    numbers.append(i)
for j in range(1, N + 1, 2):
    numbers.append(j)
print(numbers)
print(numbers[K - 1])


"""for i in range(2, N + 1, 2):
    print(i, end=' ')
for j in range(1, N + 1, 2):
    print(j, end=' ')"""