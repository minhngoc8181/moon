# https://laptrinh.codemath.vn/problem/xau_kv25n

s = input()


def check(end):
    setChar = {s[end], s[end - 1], s[end - 2], s[end - 3]}
    return len(setChar) >= 3


count = 0
start = 0
while start < len(s) - 3:
    end = start + 3
    while end < len(s) and check(end):
        end += 1
    length = end - start
    if length >= 4:
        count += (length - 3) * (length - 2) // 2
    start = end - 2
print(count)
