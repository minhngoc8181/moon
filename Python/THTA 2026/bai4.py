N, K = map(int, input().split())

num1s = []
num2s = []
num3s = []

for i in range(1, N + 1):
    if i % 2 == 0:
        num1s.append(i)
    elif i % 3 == 0:
        num2s.append(i)
    else:
        num3s.append(i)

nums = num1s + num2s + num3s

print(nums)

print(sum(nums[:K]))
