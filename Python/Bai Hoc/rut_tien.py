M = int(input())
count = 0
count += M // 100
M -= M // 100 * 100
count += M // 50
M -= M // 50 * 50
count += M // 20
M -= M // 20 * 20
count += M // 10
M -= M // 10 * 10
count += M // 5
M -= M // 5 * 5
count += M // 2
M -= M // 2 * 2
count += M // 1
M -= M // 1 * 1
count += M
print(count)


M = int(input())
count = 0
for d in [100, 50, 20, 10, 5, 2, 1]:
    count += M // d
    M -= M // d * d
print(count)
