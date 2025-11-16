# https://laptrinh.codemath.vn/problem/dovuitinhoc

N, K = map(int, input().split())
numbers = []
for i in range(N):
    numbers.append(int(input()))

counts = [1] * N
for i in range(N):
    number = numbers[i]
    for j in range(i):
        if numbers[j] + K <= number:
            counts[i] = max(counts[i], counts[j] + 1)

print(max(counts))
