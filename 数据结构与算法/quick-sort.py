import random
def quick_sort(arr):
    """
    快速排序
    """
    if not arr:
        return []
    pivot = arr[0]
    left  = [x for x in arr     if x <  pivot]
    right = [y for y in arr[1:] if y >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

l1 = [3,5,2,7,6,8,1,10,9]
print(quick_sort(l1))