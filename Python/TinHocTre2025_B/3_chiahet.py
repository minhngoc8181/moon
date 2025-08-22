def is_better(s1, s2):
    if s2 is None:
        return True
    if len(s1) > len(s2):
        return True
    if len(s1) < len(s2):
        return False
    return s1 > s2


def solve():
    a, m_str = input().split()
    m = int(m_str)
    n = len(a)

    dp = [None] * m

    for digit_char in a:
        digit_val = int(digit_char)

        next_dp = dp[:]

        if digit_val != 0:
            rem = digit_val % m
            if is_better(digit_char, next_dp[rem]):
                next_dp[rem] = digit_char

        for j in range(m):
            if dp[j] is not None and dp[j] != "0":
                new_num_str = dp[j] + digit_char
                new_rem = (j * 10 + digit_val) % m

                if is_better(new_num_str, next_dp[new_rem]):
                    next_dp[new_rem] = new_num_str

        dp = next_dp

    final_ans = dp[0]
    if "0" in a:
        if is_better("0", final_ans):
            final_ans = "0"

    if final_ans is None:
        print("!")
    else:
        print(final_ans)


T = int(input())
for _ in range(T):
    solve()
