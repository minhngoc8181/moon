A, B = map(int, input().split())
min_value = A * B
for i in range(8, 26):
    area = A * B
    collum = A // i
    row = B // i
    areaAB = row * collum * i * i
    ans = area - areaAB
    # ans = A * B - (A // i) * (B // i) * i * i
    if min_value > ans:
        min_value = ans
print(min_value)