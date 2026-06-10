N, T = map(int, input().split())
nums = list(map(int, input(). split()))
total = 0
count = 0
for i in nums:
    if i >= T:
        total += 100
        count += 1
    else:
        total -= 50
        count = 0
    if count >= 3:
        total += 200
print(total)