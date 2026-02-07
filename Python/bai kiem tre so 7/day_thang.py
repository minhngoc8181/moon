K = int(input())
numbers = []
for no0fDigit in range(2, 30):
    if len(numbers) > K:
        break
    for c in "12346789":
        new_number = int(c + "5" * (no0fDigit - 1))
        numbers.append(new_number)
    for p in range(1, no0fDigit):
        for c in "012346789":
            new_number = int("5" * p + c + "5" * (no0fDigit - p - 1))
            numbers.append(new_number)
numbers.sort()
print(numbers[K - 1])