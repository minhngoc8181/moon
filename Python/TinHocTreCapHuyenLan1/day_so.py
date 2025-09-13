n = int(input())
count = 0
"""num = 0
for i in range(1, n + 1):
    num += i
    if num % 6 == 0:
        count += 1
print(count)"""

for i in range(1, n + 1):
    num = (1 + i) * i / 2
    if num % 6 == 0:
        count += 1
print(count)
