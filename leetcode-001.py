class Solution(object):
    """
    1.实现一个算法，确定一个字符串s的所有字符是否全都不同
    简单粗暴的办法，直接set对字符串去重，比较长度
    """
    def isUnique(self, astr):
        """
        :type astr: str
        :rtype: bool
        """
        if len(astr) == len(set(astr)):
            return True
        else:
            return False

a = Solution().isUnique(None)
print(a)