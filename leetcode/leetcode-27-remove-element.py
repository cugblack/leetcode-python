# 27. 移除元素
# https://leetcode-cn.com/problems/remove-element/

def remove_element_1(nums, val) -> int:
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    ans = 0
    for i in nums:
        if i != val:
            nums[ans] = i
            ans += 1
    return ans


def remove_element_2(nums, val) -> int:
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    fast = 0
    slow = 0

    while fast < len(nums):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    return slow


