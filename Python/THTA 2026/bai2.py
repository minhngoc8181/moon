X = int(input())
ans = []
for i in range(1, 10):
    for j in range(2, 10):
        if i * j == X:
            ans.append(i)
            print(ans[0])
            break
if len(ans) == 0:
    print(0)