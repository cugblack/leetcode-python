class Solution(object):
    """
    确定其中一个字符串的字符重新排列后，能否变成另一个字符串
    1.判断两个字符串长度是否相同，不同则为False
    2.长度相同，则判断两字符串中所有元素出现的次数，完全相同则为True
    """
    def CheckPermutation(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
            return False
        b = set(s1)
        for i in b:
            if s1.count(i) != s2.count(i):
                return False
        return True
a = Solution().CheckPermutation("abd", "adb")
print(a)