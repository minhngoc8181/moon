numbers = list(map(int, input().split()))
maxValue = numbers[0]
for num in numbers:
    if num > maxValue:
        maxValue = num
print(maxValue)