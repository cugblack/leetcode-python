#2104. 子数组范围和
#https://leetcode.cn/problems/sum-of-subarray-ranges/

import math
def subArrayRanges(nums):
    
    n = len(nums)
    if n <= 1:
        return 0
    ans = 0

    for i in range(n):
        print(i)
        minVal, maxVal = math.inf, -math.inf
        for j in range(i, n):
             minVal = min(minVal, nums[j])
             maxVal = max(maxVal, nums[j])
             ans += maxVal-minVal
    return ans

nums=[1,2,3]
print(subArrayRanges(nums))
