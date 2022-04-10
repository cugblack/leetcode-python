def insert_sort(arr):
    """
    1、从第一个元素开始，该元素可以认为已经被排序；
    2、取出下一个元素，在已经排序的元素序列中从后向前扫描；
    3、如果该元素（已排序）大于新元素，将该元素移到下一位置；
    4、重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
    5、将新元素插入到该位置后；
    6、重复步骤2~5。
    """
    length = len(arr)
    for i in range(1, length):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(arr)
    return arr


l1 = [5, 4, 6, 8, 7, 10, 9, 3, 23, 20]

print(insert_sort(l1))
