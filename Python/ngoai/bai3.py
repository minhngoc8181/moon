L, R = map(int, input().split())
nums = []
for i in range(1, R + 1):
    nums.extend(range(1, i + 1))
    if len(nums) > R:
        break
# print(nums)
print(sum(nums[L - 1: R]))