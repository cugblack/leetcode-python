# 88. 合并两个有序数组
# https://leetcode-cn.com/problems/merge-sorted-array/

def merge_1(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    连个数组都有序，直接追加后重新排序
    """
    nums1[m:] = nums2
    nums1.sort()


def merge_2(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    双指针：注意处理临界条件
    """
    p1, p2 = 0, 0
    sorted = []
    while p1 < m or p2 < n:
        if p1 == m:
            sorted.append(nums2[p2])
            p2 += 1
        elif p2 == n:
            sorted.append(nums1[p1])
            p1 += 1
        elif nums1[p1] < nums2[p2]:
            sorted.append(nums1[p1])
            p1 += 1
        else:
            sorted.append(nums2[p2])
            p2 += 1
    nums1[:] = sorted