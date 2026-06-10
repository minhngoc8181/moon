K = int(input())
S = input()
ans = ''
is_ok = 1
for c in 'abcdefghijklmnopqrstuvwxyz':
    count = S.count(c)
    if count % K == 0:
        ans += c * (count // K)
    else:
        print(-1)
        is_ok = 0
        break
if is_ok == 1:
    print(ans * K)