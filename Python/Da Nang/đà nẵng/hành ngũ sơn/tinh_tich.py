N = int(input())
nums = list(map(int, input().split()))
maxvalue = 0
left = 0
right = sum(nums)
for i in range(0, len(nums)):
    left += nums[i]
    right -= nums[i]
    ans = left * right
    if ans > maxvalue:
        maxvalue = ans
print(maxvalue)

# print((sum(numbers) - N - N + 1) * (N + N - 1)) 