text = input()
text_length = len(text)
start = -1
maxDigit = int(text[-1])
for i in range(text_length - 2, -1, -1):
    digit = int(text[i])
    maxDigit = max(maxDigit, digit)
    if maxDigit > digit:
        start = i

if start == -1:
    print(text)
else:
    maxDigit = int(text[start])
    for i in range(start, text_length):
        maxDigit = max(maxDigit, int(text[i]))
    max_text = text
    for i in range(text_length - 1, start, -1):
        digit = int(text[i])
        if digit == maxDigit:
            new_text = text[:start] + text[start : i + 1][::-1] + text[i + 1 :]
            if new_text > max_text:
                max_text = new_text
    print(max_text)
