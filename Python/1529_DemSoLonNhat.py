numbers = list(map(int, input().split()))
maxValue = numbers[0]
for num in numbers:
    if num > maxValue:
        maxValue = num
count = 0
for i in numbers:
    if i == maxValue:
        count += 1
print(count)