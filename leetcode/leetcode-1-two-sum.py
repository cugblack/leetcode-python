# 1. 两数之和
# https://leetcode-cn.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target: int):
        if not nums:
            return -1
        for i in range(len(nums)):
            num = target - nums[i]
            if num in nums and i != nums.index(num):
                return [i, nums.index(num)]


nums = [3, 3]
target = 6

l = Solution()
print(l.twoSum(nums, target))
