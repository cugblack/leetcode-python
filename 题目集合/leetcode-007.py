class Solution(object):
    """
    给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
    请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
    你可以假设 nums1 和 nums2 不会同时为空。

    list.extent() 在列表末尾一次性追加另一个序列中的多个值
    1.合并两数组并重新排序
    2.新数组长度为奇数：取 len//2 位置的值；偶数取(len//2 + len//2+1)/2.0的值

    """
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if nums1 or nums2:
            nums1.extend(nums2)
            nums1.sort()
        if len(nums1) %2 ==0:
            return (nums1[len(nums1)//2] + nums1[len(nums1)//2 -1])/2.0
        else:
            return float(nums1[len(nums1)//2])
print(Solution().findMedianSortedArrays([1,3], [2]))