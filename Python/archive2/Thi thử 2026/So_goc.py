N = int(input())
number = 2
step = 2
for i in range(1, N + 1):
    number += step
    if i % 2 == 0:
        step += 2
print(number)



N = int(input())
start = 4
end = (N // 2) * 4
distance = (start + end) * (N // 2) // 2
if N % 2 == 0:
    print(2 + distance)
else:
    print(2 + distance + (N + 1) // 2 * 2)