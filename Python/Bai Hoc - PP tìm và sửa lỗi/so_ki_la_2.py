N = int(input())
divisors = []
for i in range(2, N):
    if (N // i) == (N % i):
        divisors.append(i)

print(f'{len(divisors)}:{" ".join(map(str, divisors))}')
