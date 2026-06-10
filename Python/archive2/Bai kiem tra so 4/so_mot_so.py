N = int(input())
count = 0
for i in range(1, 10 + 1):
    for j in range(1, 9 + 1):
        if int(str(j) * i) <= N:
            count += 1
print(count)
# print(str(j) * i)
