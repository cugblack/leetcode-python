# 605. 种花问题
# https://leetcode-cn.com/problems/can-place-flowers/

from typing import List


def can_place_flowers(flowerbed: List[int], n: int) -> bool:
    """
    input:
        flowerbed: 数组，只包含0、1
        n: 需要种植的花 数量
    output：
        bool: 能否种植
    思路：
        1） m为数组长度， count为可种植的数量， prev为上一次1出现的下标
        2） 遍历数组
        2） 判断：
            当前位置为1，则判断prev的值，即上次1出现的位置，
                首次出现1，则当前的区域可种植数量为（i//2）；
                非首次出现1，则当前区域可种植数量为（i-prev-2）//2,【-2是为了去除边界的位置】
                对区域可种植数量进行累加
            循环中，如果count >= n, 直接返回
            循环结束，需要判断：
                如果未出现过1，即prev<0,则全0数组可种植数量为（m+1）//2
                如出现过，则计算最后一个区间的可种植数量（m-prev-1）【只有左侧有边界，右侧无】
        3)  比较count和期望值n
    """
    count = 0
    prev = -1
    m = len(flowerbed)
    for i in range(m):
        if flowerbed[i] == 1:
            if prev < 0:
                count += i // 2
            else:
                count += (i - prev - 2) // 2
            prev = i
        if count >= n:
            return True
    if prev < 0:
        count += (m + 1) // 2
    else:
        count += (m - prev - 1) // 2
    return count >= n


if __name__ == "__main__":
    flowerbed = [1, 0, 0, 0, 1, 0, 0]
    n = 2
    print(can_place_flowers(flowerbed, n))
