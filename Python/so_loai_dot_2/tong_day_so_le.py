N = int(input())
for i in range(1, N + 1):
    while(i % 2 == 0):
        i //= 2
    total += i
print(total)