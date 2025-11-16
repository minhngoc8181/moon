# https://laptrinh.codemath.vn/problem/socobauoc
import math


def isPrime(n):
    limit = math.floor(math.sqrt(n))
    for i in range(2, limit + 1):
        if n % i == 0:
            return False

    return True


N = int(input())
maxPrime = math.floor(math.sqrt(N))

count = 0
for i in range(2, maxPrime + 1):
    if isPrime(i) and i * i <= N:
        count += 1

print(count)
