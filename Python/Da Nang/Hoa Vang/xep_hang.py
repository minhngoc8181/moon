N = int(input())
K = int(input())
list_value = []
for i in range(1, N + 1):
    if i % 5 == 0:
        list_value.append(i)
for j in range(1, N + 1):
    if j % 3 == 0 and j % 5 != 0:
        list_value.append(j)
for l in range(1, N + 1):
    if l % 3 != 0 and l % 5 != 0:
        list_value.append(l)
print(list_value[K - 1])