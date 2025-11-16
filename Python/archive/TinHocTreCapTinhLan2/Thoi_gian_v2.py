T = int(input())
hours = 8 + (T // 60)
minutes = T % 60
print(f"{hours:02.0f}:{minutes:02.0f}")
