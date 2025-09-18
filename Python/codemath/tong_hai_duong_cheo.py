# https://laptrinh.codemath.vn/problem/thdc_hn25

m = int(input())
n = int(input())
X = int(input())
Y = int(input())

count1 = min(X, n + 1 - Y)
count1 += min(Y - 1, m - X)

deltaleft = min(X, Y) - 1
startX = X - deltaleft
startY = Y - deltaleft
deltaRight = min(m - X, n - Y)

sum2 = (
    # (start + end)*noItem // 2 = (start + start + distance * intervals) * (intervals + 1) // 2
    (startX + startY + startX + startY + 2 * (deltaleft + deltaRight))
    * (deltaleft + deltaRight + 1)
    // 2
)

print(count1 * (X + Y) + sum2 - X - Y)
