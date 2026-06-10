a = int(input())
b = int(input())
total = 0
for i in range(a + 1, b):
    if i % 2 == 0:
        total += i
print(total)


print(sum(range(a + 1, b)))