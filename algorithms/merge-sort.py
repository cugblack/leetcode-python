from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    """
    把长度为n的输入序列分成两个长度为n/2的子序列；
    对这两个子序列分别采用递归的进行排序；
    """
    import math
    if len(arr) < 2:
        return arr
    middle = math.floor(len(arr) / 2)
    left, right = arr[0:middle], arr[middle:]
    return merge(merge_sort(left), merge_sort(right))


def merge(left: List[int], right: List[int]) -> List[int]:
    """
    将两个排序好的子序列的元素拿出来，按照顺序合并成一个最终的序列，即可完成排序
    """
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


l1 = [3, 1, 4, 2, 6, 7, 9, 8, 10]
print(merge_sort(l1))
