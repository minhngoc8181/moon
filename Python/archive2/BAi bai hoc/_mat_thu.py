S = input()
m = 1
for i in range(0, len(S)):
    for j in range(i, len(S)):
        sub = S[i : j]
        if sub == sub[::- 1]:
            if len(sub) > m:
                m = len(sub)
print(sub)