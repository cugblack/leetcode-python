class Solution(object):
    """
    给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度
    """
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        滑动窗口，维护记录当前窗口长度的cur_len和最大窗口长度的max_len,一旦出现重复字串，窗口清空从0开始
        """
        cur_len = 0
        max_len = 0
        l = []
        for i in range(len(s)):
            if s[i] not in l:
                l.append(s[i])
                cur_len += 1
            else:
                idx = l.index(s[i])
                l = l[idx+1:]
                l.append(s[i])
                cur_len = len(l)
            if cur_len > max_len:
                max_len = cur_len
        return max_len
print(Solution().lengthOfLongestSubstring('abccdef'))

