N_str = input()
N_len = len(N_str)
if len(N_str) % 2 == 0:
    if N_str[: N_len // 2] == N_str[N_len // 2:]:
        print("Yes")
    else:
        print("No")
# print(N_str[: N_len // 2])
# print(N_str[N_len // 2:])

N_str = input()
N_len = len(N_str)
if len(N_str) % 2 == 0 and N_str[: N_len // 2] == N_str[N_len // 2:]:
    print("Yes")
else:
    print("No")