import math
n = int(input())

if math.sqrt(n) - math.floor(math.sqrt(n)) == 0:
    print(1)
else:
    print(0)
