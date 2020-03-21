class Solution(object):
    """
    将字符串中的空格全部替换为%20。假定该字符串尾部有足够的空间存放新增字符，并且知道字符串的“真实”长度。
    """
    def replaceSpaces(self, S, length):
        """
        :type S: str
        :type length: int
        :rtype: str
        """
        return S[:length].replace(" ", "%20")

a = Solution().replaceSpaces("my name     ", 8)
print(a)