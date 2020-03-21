class Solution(object):
    """
    给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
    你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

    enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
    1.维护一个存放数组值(key)和索引(value)的字典
    2.用目标数减去数组中元素，如果结果在字典中，则返回值和索引，不在则将元素加入字典
    """
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #             if nums[j] + nums[i] == target and i != j:
        #                 return i,j
        hashmap = {}
        for idx, val in enumerate(nums):
            if target - val in hashmap:
                return hashmap[target-val], idx
            else:
                hashmap[val] = idx


print(Solution().twoSum([1,2,3,1,4], 5))