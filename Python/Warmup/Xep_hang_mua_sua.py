N = int(input())
nums = list(map(int, input().split()))
count = 0
A = 1
for i in nums:
    if i != A:
        count += 1
    if i == A:
        A += 1
print(count)