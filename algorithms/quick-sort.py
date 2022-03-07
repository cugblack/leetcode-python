import random
def quick_sort(arr):
    """
    快速排序，实现1
    """
    if not arr:
        return []
    pivot = arr[0]
    left  = [x for x in arr     if x <  pivot]
    right = [y for y in arr[1:] if y >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


def patition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quick_sort_2(arr, low, high):
    if low < high:
        pivot = patition(arr, low, high)
        quick_sort_2(arr, low, pivot-1)
        quick_sort_2(arr, pivot, high)


l1 = [3,5,2,7,6,8,1,10,9,4]
print(quick_sort(l1))
print(l1)

quick_sort_2(l1, 0, len(l1)-1)
print(l1)