class Solution(object):
    """
    最长上升子序列

    """
    def findMedianSortedArrays(self, s):
        """
        :type nums1: List[int]
        :rtype: float

        维护len(s)个数组，分别表示 从数组第一个元素到 数组i元素结尾的子序列的长度
        """
        length = len(s)
        if length < 2:
            return False
        dp = [1] * length

        for i in range(1, length):

            for j in range(i):
                if s[j] < s[i]:
                    dp[i] = max(dp[i], dp[j]+1)
            print(dp)
        return max(dp)
print(Solution().findMedianSortedArrays([2,3,4,5,1,2,3,6,7,8,3,6,7]))
        