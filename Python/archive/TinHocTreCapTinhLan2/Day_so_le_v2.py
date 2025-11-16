N = int(input())
K = int(input())
numbers = list(range(2, N + 1, 2))
numbers.extend(list(range(1, N + 1, 2)))
print(numbers[K - 1])


"""for i in range(2, N + 1, 2):
    print(i, end=' ')
for j in range(1, N + 1, 2):
    print(j, end=' ')"""
