def bubble_sort(arr):
    """
    冒泡排序：比较相邻的元素。如果第一个比第二个大，
    就交换他们两个，这样每次可以把未排序空间的最大元素
    移动到已排序空间的最前面
    """
    length = len(arr)
    for i in range(length):
        for j in range(0, length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


l1 = [1, 3, 2, 27, 4, 5, 7, 9, 5, 4]
print(bubble_sort(l1))
