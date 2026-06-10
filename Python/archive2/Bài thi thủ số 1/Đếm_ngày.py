A = int(input())
B = int(input())
KC = B - A
if KC <= 0:
    print(0)
elif KC == 1:
    print(2)
else:
    print(KC // 2 + 1)