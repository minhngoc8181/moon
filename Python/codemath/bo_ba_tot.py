# https://laptrinh.codemath.vn/problem/bobatot

n = int(input())
numbers = list(map(int, input().split()))

numbers.sort()
count = 0
for i in range(n):
    if i > 0 and numbers[i] == numbers[i - 1]:
        continue
    k = 0
    for j in range(i + 1, n):
        if j != i + 1 and numbers[j] == numbers[j - 1]:
            continue
        sum = numbers[i] + numbers[j]
        while k < n:
            if sum == numbers[k]:
                count += 1
                k += 1
            elif sum < numbers[k]:
                break
            else:
                k += 1
print(count)
