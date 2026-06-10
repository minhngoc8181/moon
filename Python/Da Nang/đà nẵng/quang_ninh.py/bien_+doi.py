S = list(input())
count = 0
for i in range(2, len(S)):
    if S[i] == S[i - 2] and S[i] == S[i - 1]:
        count += 1
        S[i] = '1'
print(count)