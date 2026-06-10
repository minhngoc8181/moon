import sys

# Thiết lập giới hạn mới là 5000 cấp
sys.setrecursionlimit(5000)

N, K, S = map(int, input().split())


def process(maxNum, selectedNums, sumNum):
    global K
    if K <= 0:
        return
    for j in range(maxNum, 0, -1):
        if K <= 0:
            return
        if j + sumNum == S:
            K -= 1
            print(*(selectedNums + [j, 0]))
        elif j + sumNum < S:
            process(j - 1, selectedNums + [j], sumNum + j)


preNums = []
sum = 0
for i in range(N, 1000, -1):
    if sum + 1000 > S:
        break
    else:
        preNums.append(i)
        sum += i
        N -= 1

process(N, preNums, sum)
