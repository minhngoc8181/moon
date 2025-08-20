""" numbers = list(map(int, input().split()))
count = 0
for i in numbers:
    if i % 2 == 1:
        count += 1
print(count) """

M = int(input())
numbers = list(map(int, input().split()))
count = 0
for i in numbers:
    if i == M:
        count += 1
print(count)