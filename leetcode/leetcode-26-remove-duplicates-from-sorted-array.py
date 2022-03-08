# 26. 删除有序数组中的重复项
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

# def remove_duplicates(nums):
#     tmp = []
#     for i in nums:
#         if i not in tmp:
#             tmp.append(i)
#     return len(tmp), tmp

def remove_duplicates(nums):
    len1 = len(nums)
    if len1 <= 0:
        return 0
    fast = slow = 1
    while fast < len1:
        if nums[fast] != nums[fast - 1]:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    return slow


nums = [1, 1, 2, 2, 3, 4]

print(remove_duplicates(nums))
