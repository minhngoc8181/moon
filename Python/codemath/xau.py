# https://laptrinh.codemath.vn/problem/xau_kv25n

s = input()


def check(end):
    setChar = {s[end], s[end - 1], s[end - 2], s[end - 3]}
    return len(setChar) >= 3


count = 0
for start in range(len(s) - 4):
    for end in range(start + 3, len(s)):
        if check(end):
            count += 1
        else:
            break

print(count)
