# 14. 最长公共前缀
# https://leetcode-cn.com/problems/longest-common-prefix/
class Solution:
    """
    求解思路： 找到最短串的长度min_len，遍历每个数组元素的[0,min_len],不同则输出，有则继续比较
    1.长度为1的数组，输出第一个元素
    2.长度为空的数组，输出为空
    """

    def longestCommonPrefix(self, strs):
        """
        解法一：利用zip使得数组内的每个元素长度相同,并用set去重后如果长度为1则说明是公共字符，继续，否则输出
        """
        res = ""
        for sub in zip(*strs):
            if len(set(sub)) == 1:
                res += sub[0]
            else:
                break
        return res


print(Solution().longestCommonPrefix(['']))
