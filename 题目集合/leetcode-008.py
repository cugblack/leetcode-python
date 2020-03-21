class Solution(object):
    """"
    给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
    解法一：暴力破解，先找出所有的长度大于2的字串，遍历判断是否回文子串，之后比较和之前记录的最大字串的长度并更新
    """
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        length = len(s)
        max_len = 0
        for i in range(length-1):
            for j in range(i+1, length):
                if self.valid(s, i, j) and j-i+1 > max_len:
                    max_len = j - i + 1
                    res = s[i: j+1]
        return res
    
    def valid(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

print(Solution().longestPalindrome("abccdadc"))