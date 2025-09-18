# https://laptrinh.codemath.vn/problem/nghenhac

N = int(input())

songs = [[index + 1, int(time)] for index, time in enumerate(input().split())]
songs.sort(key=lambda s: s[1])

total = 0
for i in range(N):
    total += songs[i][1] * (N - i)
    print(*songs[i])

print(total)
