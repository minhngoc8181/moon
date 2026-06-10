import math

A = int(input())
B = int(input())
C = int(input())
D = int(input())
tong = (A + B) * (B - A + 1) // 2

s1 = (A + C - 1) // C * C
e1 = B - (B % C)
sh1 = (e1 - s1) // C + 1
t1 = (s1 + e1) * sh1 // 2

s2 = (A + D - 1) // D * D
e2 = B - (B % D)
sh2 = (e2 - s2) // D + 1
t2 = (s2 + e2) * sh2 // 2

# CD = C * D
CD = C * D // math.gcd(C, D)
s3 = (A + CD - 1) // CD * CD
e3 = B - (B % CD)
sh3 = (e3 - s3) // CD + 1
t3 = (s3 + e3) * sh3 // 2

skch = t1 + t2 - t3
print(tong - skch)