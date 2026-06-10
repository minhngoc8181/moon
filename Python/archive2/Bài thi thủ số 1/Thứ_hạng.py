A, B, C, D = map(int, input().split())
total = 0

if A > B:
    total += 1
if A > C:
    total += 1
if A > D:
    total += 1
print(4 - total)


numbers = list(map(int, input().split()))
A = numbers[0]
numbers.sort(reverse=True)
print(numbers.index(A) + 1)


numbers = list(map(int, input().split()))
A = numbers[0]
print(len([x for x in numbers if x > A]) + 1)
