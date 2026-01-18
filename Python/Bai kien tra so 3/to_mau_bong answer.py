import math

N = int(input())
a = int(input())
b = int(input())

red = N // a
green = N // b
bcnn = a * b // math.gcd(a, b)
yellow = N - red - green + N // bcnn
print(yellow)
