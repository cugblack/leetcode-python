def merge(l,r):
    """
    数组合并并且排序
    """
    length = len(l) + len(r)
    # 防止 循环length次 导致IndexError: list index out of range
    l.append(float("inf"))
    r.append(float("inf"))

    A = []
    i,j = 0,0
    for k in range(length):
        if l[i] <= r[j]:
            A.append(l[i])
            i += 1
        else:
            A.append(r[j])
            j += 1
    return A

def merge_sort(arr):
    """
    归并排序
    """
    length = len(arr)
    if length <= 1:
        return arr
    else:
        mid = length // 2
        left = merge_sort(arr[0:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)

l1 = [3,1,4,2,6,7,9,8,10]
print(merge_sort(l1))