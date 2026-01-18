A = int(input())
B = int(input())
total = 0
for i in range(A, B + 1):
    if i % 3 == 0 and i % 5 != 0:
        total += i
print(total)