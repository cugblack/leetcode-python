# 3. 无重复字符的最长子串
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

def length_of_longest_substring(s: str) -> int:

    max_len = 0
    tmp = []
    for i in range(len(s)):

        while s[i] in tmp:
            del tmp[0]
        tmp.append(s[i])
        if max_len < len(tmp):
            max_len = len(tmp)
    return max_len

