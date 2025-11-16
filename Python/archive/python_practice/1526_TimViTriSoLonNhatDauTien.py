"""M = int(input())
number = list(map(int, input().split()))
found = False
for position in range(len(number)):
    if number[position] == M:
        print(position)
        found = True
        break
if found == False:
    print(-1)
"""
"""numbers = list(map(int, input().split()))
maxValue = numbers[0]
for num in numbers:
    if num > maxValue:
        maxValue = num
print(maxValue)"""


numbers = list(map(int, input().split()))
maxValue = numbers[0]
for num in numbers:
    if num > maxValue:
        maxValue = num
for position in range(len(numbers)):
    if numbers[position] == maxValue:
        print(position)
        break