def bubble_sort(arr):
    """
    冒泡排序
    """
    length = len(arr)
    for i in range(length):
        for j in range(0, length - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

l1 = [1,3,2,27,4,5,7,9,5,4]
print(bubble_sort(l1))