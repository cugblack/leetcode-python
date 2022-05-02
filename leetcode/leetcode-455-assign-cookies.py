# 455. 分发饼干
# https://leetcode-cn.com/problems/assign-cookies/

from typing import List


def find_content_children(g: List[int], s: List[int]) -> int:
    """
    input:
        g[i]: 小孩 i 的 胃口值
        s[j]: 饼干 j 的 大小
    output：
        count: 被满足的小孩子数量

    思路：
    1） 先对g、s进行排序
    2） 遍历g、s，直到饼干被分完或者所有小孩的胃口被满足
    3） 每块饼干只能分给最多一个小孩
    """
    g.sort()
    s.sort()

    m = len(g)
    n = len(s)

    i = j = count = 0

    while i < m and j < n:
        while j < n and g[i] > s[j]:
            j += 1
        if j < n:
            count += 1
        i += 1
        j += 1
    return count


if __name__ == "__main__":
    g = [1, 2, 3]
    s = [1, 1, 6]
    print(find_content_children(g, s))
