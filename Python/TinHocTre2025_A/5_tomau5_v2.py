M = int(input())
N = int(input())
count = 0
for i in range(M):
    start = N * i + 1
    end = start + N - 1
    start_multiple_5 = ((start + 4) // 5) * 5
    end_multiple_5 = (end // 5) * 5
    """if (
        start <= start_multiple_5
        and start_multiple_5 <= end
        and start_multiple_5 > end_multiple_5
    ):
        print(
            f"Something is wrong? {i} {start} {end} {start_multiple_5} {end_multiple_5}"
        )"""
    if start <= start_multiple_5 and start_multiple_5 <= end:
        numOfItem = (end_multiple_5 - start_multiple_5) / 5 + 1
        count += (
            (start_multiple_5 - start + 1 + end_multiple_5 - start + 1) * numOfItem / 2
        )
        count += i * numOfItem
        count %= 2025
print(round(count))
