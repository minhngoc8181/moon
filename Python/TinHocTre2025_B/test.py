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

    # dp[j] lưu chuỗi số lớn nhất có số dư là j khi chia cho m
    dp = [None] * m

    # Duyệt qua từng chữ số của chuỗi a
    for digit_char in a:
        digit_val = int(digit_char)

        # next_dp để lưu các kết quả của bước hiện tại
        next_dp = dp[:]

        # Lựa chọn 1: Bắt đầu một số mới bằng chữ số hiện tại (nếu khác 0)
        if digit_val != 0:
            rem = digit_val % m
            if is_better(digit_char, next_dp[rem]):
                next_dp[rem] = digit_char

        # Lựa chọn 2: Thêm chữ số hiện tại vào cuối các số đã có
        for j in range(m):
            if dp[j] is not None and dp[j] != "0":
                new_num_str = dp[j] + digit_char
                new_rem = (j * 10 + digit_val) % m

                if is_better(new_num_str, next_dp[new_rem]):
                    next_dp[new_rem] = new_num_str

        dp = next_dp

    # Trường hợp đặc biệt: số 0
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
