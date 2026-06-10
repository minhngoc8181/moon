K = int(input())
digit_text = "123456789101112" * (K // 15 + 1)
total = 0
for i in range(K):
    total += int(digit_text[i])
print(total)