def insert_sort(arr):
    """
    插入排序，数据分为已排序空间和未排序空间，
    初始情况下已排序空间仅有第一个元素，往后
    依次从未排序空间取值和已排序空间的值比较
    并插入对应的位置
    """
    length = len(arr)
    for i in range(1,length):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        print(arr)
    return arr

l1 = [5,4,6,8,7,10,9,3,23,20]

print(insert_sort(l1))