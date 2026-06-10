L = int(input())
R = int(input())
tong1 = (1 + R) * R // 2
if R % 6 == 4:
    tong1 += 2
elif R % 6 == 5:
    tong1 += 2

R = L - 1
tong2 = (1 + R) * R // 2
if R % 6 == 4:
    tong2 += 2
elif R % 6 == 5:
    tong2 += 2

print(tong1 - tong2)