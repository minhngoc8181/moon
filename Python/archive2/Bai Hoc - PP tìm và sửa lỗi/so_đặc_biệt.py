count = 0
for i in range(1, 2024):
    if i % 14 == 5 and i % 15 == 4:
        count += 1
print(count)