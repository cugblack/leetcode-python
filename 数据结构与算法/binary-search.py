class BinarySearch(object):
    """
    二分查找，有序数组
    """
    def binary_search(self, arr, key):
        """
        简单版，无变形
        """
        if not arr:
            return False
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = low + ((high - low) >> 1)
            guess = arr[mid]
            if guess == key:
                return mid
            elif guess > key:
                high = mid - 1
            else:
                low = mid + 1
        return False


    def binary_search_1(self, arr, key):
        """
        变形1：查找第一个等于给定值的元素
        """
        if not arr:
            return False
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = low + ((high - low) >> 1)
            guess = arr[mid]
            if guess == key:
                if arr[mid-1] != guess or mid == 0:
                    return mid
                else:
                    high = mid - 1
            elif guess > key:
                high = mid - 1
            else:
                low = mid + 1
        return False

    def binary_search_2(self, arr, key):
        """
        变形2：查找最后一个等于给定值的元素
        """
        if not arr:
            return False
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = low + ((high - low) >> 1)
            guess = arr[mid]
            if guess == key:
                if arr[mid+1] != guess or mid == len(arr) - 1:
                    return mid
                else:
                    low = mid + 1
            elif guess > key:
                high = mid -1
            else:
                low = mid + 1
        return False

    def binary_search_3(self, arr, key):
        """
        变形3：查找第一个大于等于给定值的元素
        """
        if not arr:
            return False
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = low + ((high - low) >> 1)
            guess = arr[mid]
            if guess >= key:
                if mid == 0 or arr[mid -1] < key:
                    return mid
                high = mid -1
            else:
                low = mid + 1
        return False

    def binary_search_4(self, arr, key):
        """
        变形3：查找最后一个小于等于给定值的元素
        """
        if not arr:
            return False
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = low + ((high - low) >> 1)
            guess = arr[mid]
            if guess <= key:
                if arr[mid+1] > guess or mid == len(arr)-1:
                    return mid
                else:
                    low = mid + 1
            else:
                high = mid - 1
        return False        

l1 = [2,4,5,7,8,10,22,22,22,22,22,22,23,25,33,44,66,77]

# 普通二分查找
print(BinarySearch().binary_search(l1, 22))
# 查找第一个等于给定值的元素
print(BinarySearch().binary_search_1(l1, 22))
# 查找最后一个等于给定值的元素
print(BinarySearch().binary_search_2(l1, 22))
# 查找第一个大于给定值的元素
print(BinarySearch().binary_search_3(l1, 9))
# 查找最后一个小于给定值的元素
print(BinarySearch().binary_search_4(l1, 9))