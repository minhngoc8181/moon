N = input()
maxvalue = 0
for i in range(1, len(N)):
    left = N[: i]
    right = N[i :]
    ans = int(left) * int(right)
    if ans > maxvalue:
        maxvalue = ans
print(maxvalue)