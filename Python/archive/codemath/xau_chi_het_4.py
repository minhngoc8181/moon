# https://laptrinh.codemath.vn/problem/lhp18xauchiahetcho4

digits = [int(c) for c in input()]
count = 0
for i in range(len(digits) - 1, -1, -1):
    if digits[i] % 4 == 0:
        count += 1
    if i > 0 and (digits[i - 1] * 10 + digits[i]) % 4 == 0:
        count += i
print(count)
