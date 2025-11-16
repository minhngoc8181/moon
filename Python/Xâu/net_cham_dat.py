count = 0
str = input()
for c in str:
    if c in 'A':
        count += 2
    elif c in 'H':
        count += 2
    elif c in 'F':
        count += 1
    elif c in 'F':
        count += 1
    elif c in 'I':
        count += 1
    elif c in 'K':
        count += 2
    elif c in 'N':
        count += 2
print(count)