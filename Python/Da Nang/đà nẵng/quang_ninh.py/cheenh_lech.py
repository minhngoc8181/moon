N = int(input())
nums = []
for i in range(1, N + 1):
    num = int(input())
    nums.append(num)

# 1 2 3 4 5 4 2 3 5 4 3 7 6 5 3 5 4 6
# | 1 2 3 4 5 4 2 3 5 4 3 7 6 5 3 5 4 6
# 1 | 2 3 4 5 4 2 3 5 4 3 7 6 5 3 5 4 6
# 1 2 | 3 4 5 4 2 3 5 4 3 7 6 5 3 5 4 6
# 1 2 3 | 4 5 4 2 3 5 4 3 7 6 5 3 5 4 6
totalLeft = 0
totalRight = sum(nums)
minValue = totalRight
minIndex = 1
for i in range(0, len(nums)):
    totalLeft += nums[i]
    totalRight -= nums[i]
    ans = abs(totalRight - totalLeft)
    if minValue > ans:
        minValue = ans
        minIndex = i
print(minIndex + 1, minValue)
