# https://laptrinh.codemath.vn/problem/ch6_kv25n

digits = [int(d) for d in input()]

length = len(digits)
if length == 1:
    print(6)
elif length == 2:
    print(96)
else:
    for i in range(length):
        if digits[i] < 9:
            digits[i] = 9
            break
    remain = sum(digits) % 3

    if digits[-1] % 2 != 0:
        remain = (9 + remain - digits[-1]) % 3
        digits[-1] = 8 if remain == 1 else 6 if remain == 0 else 4
    else:
        changed = False
        for j in range(i + 1, length - 1):
            adjust_remain = (9 + remain - digits[j]) % 3
            maxDigit = 9 if adjust_remain == 0 else 8 if adjust_remain == 1 else 7
            if digits[j] < maxDigit:
                digits[j] = maxDigit
                changed = True
                break
        if not changed:
            remain = sum(digits) % 3
            remain = (9 + remain - digits[-1]) % 3
            digits[-1] = 8 if remain == 1 else 6 if remain == 0 else 4

    print(*digits, sep="")
