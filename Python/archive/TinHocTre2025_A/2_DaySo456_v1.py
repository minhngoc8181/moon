N = int(input())
count = 0
i = 1
while count < N:
    if i % 4 != 0 and i % 5 != 0 and i % 6 != 0:
        count += 1
    i += 1

print(i - 1)
