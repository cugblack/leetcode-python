def select_sort(arr):
    """
    选择排序，分为已排序区间和未排序区间， 每次将最大或者最小的元素移动到对已排序区间的末尾
    """
    length = len(arr)
    for i in range(length):
        min_idx = i
        for j in range(i + 1, length):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(arr)
    return arr


l1 = [23, 2, 4, 1, 6, 5, 8, 7, 10, 9]
print(select_sort(l1))
