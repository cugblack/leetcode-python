class Solution:
    def longestPalindrome(self, s: str) -> str:

        max_len = 0
        tmp = []

        for i in range(len(s)):
            while s[i] in tmp:
                del tmp[0]
            tmp.append(s[i])
            if len(tmp) > max_len:
                max_len = len(tmp)
        return max_len
    
if __name__ == "__main__":

    test_str = "abbccabbcbaabbc"
    l = Solution()
    print(l.longestPalindrome(test_str))