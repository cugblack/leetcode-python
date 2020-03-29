class Solution:
    def strStr1(self, haystack, needle):
        """方式一"""
        if not needle:
            return 0
        if len(haystack) < len(needle):
            return -1
        elif len(haystack) == len(needle):
            if haystack == needle:
                return 0
            return -1
        else:

            for i in range(len(haystack) - len(needle) + 1):
                j = 1
                if haystack[i] == needle[0]:
                    while j < len(needle) and haystack[i+j] == needle[j]:
                        j += 1
                    if j == len(needle):
                        return i
            return -1

    def strStr2(self, haystack, needle):
        """方式三"""
        if not needle:
            return 0
        if len(haystack) < len(needle):
            return -1
        elif len(haystack) == len(needle):
            if haystack == needle:
                return 0
            return -1
        else:

            for i in range(len(haystack) - len(needle) + 1):
                if haystack[i:i+len(needle)] == needle:
                    return i
            return -1


    def strStr3(self, haystack, needle):
        """方法三"""
        if not needle:
            return 0
        if len(haystack) < len(needle):
            return -1
        elif len(haystack) == len(needle):
            if haystack == needle:
                return 0
            return -1
        else:
            return haystack.find(needle)

print(Solution().strStr3('hello', 'll'))
