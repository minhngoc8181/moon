M = int(input())
N = int(input())
count = 0
for start_row in range(min(5, M)):
    start = N * start_row + 1
    end = start + N - 1
    for j in range(min(5, N)):
        if (start + j) % 5 == 0:
            start_col = ((start + 4) // 5) * 5
            end_col = (end // 5) * 5
            numOfColItem = (end_col - start_col) / 5 + 1
            totalRow = (
                (start_col - start + 1 + end_col - start + 1) * numOfColItem / 2
            ) % 2025
            count += totalRow * ((M - start_row + 4) // 5)

            end_row = ((M - 1 - start_row) // 5) * 5 + start_row
            numOfRowItem = (end_row - start_row) / 5 + 1
            totalCol = ((start_row + end_row) * numOfRowItem / 2) % 2025
            count += totalCol * ((N - j + 4) // 5)

            count %= 2025
print(round(count))
