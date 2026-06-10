N = int(input())
ans = []
for i in range(1, N + 1):
    if i % 2 == 0:
        ans.extend(i)
for j in range(1, N + 1):
    if j % 3 == 0 and j % 2 != 0:
        ans.extend(j)
for d in range(1, N + 1):
    if d % 3 != 0 and d % 2 != 0:
        ans.extend(d)
print(ans)