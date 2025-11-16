N = int(input())
days = N // 1440
minutes = N % 1440

Ans = days * 3

if minutes >= 22 * 60 + 22:
    Ans += 3
elif minutes >= 11 * 60 + 11:
    Ans += 2
elif minutes >= 1:
    Ans += 1

print(Ans)