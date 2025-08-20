# 123 => 131; 1234 => 1331; 12345 => 12421; 123999456 => 124000421
text = input()
original_num = int(text)
text_length = len(text)
middle = (text_length - 1) // 2
candidates = []
candidates.append(text[: middle + 1] + "0" * (text_length - middle - 1))
for i in range(middle + 1):
    digit = int(text[i])
    if digit < 9:
        candidates.append(text[:i] + str(digit + 1) + "0" * (text_length - i - 1))

minValue = original_num * 2
for num_str in candidates:
    digits = list(num_str)
    for i in range(middle + 1):
        digits[text_length - 1 - i] = digits[i]
    new_number = int("".join(digits))
    if new_number >= original_num and new_number < minValue:
        minValue = new_number
print(minValue - original_num)
