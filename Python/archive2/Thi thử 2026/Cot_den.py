N = int(input())
K = int(input())
open = K + K
if N % open == 0:
    print(N // open)
else:
    print(N // open + 1)