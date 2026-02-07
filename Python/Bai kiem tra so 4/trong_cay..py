N = int(input())
height = 1
for i in range(1, N + 1):
    if i % 2 != 0:
        height *= 2
    else:
        height += 1
print(height)