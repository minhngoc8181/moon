N = int(input())
ans = []
for i in range(1, N + 1):
    row = list(map(int, input().split()))
    ans.append(row[i - 1])
print(ans)