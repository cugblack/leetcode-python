# 125. 验证回文串
# https://leetcode-cn.com/problems/valid-palindrome/

def isPalindrome(s: str):
    """
    :type s: str
    :rtype: bool
    """
    # 方法1： 双指针，头尾挨个判断，不相等则输出False，直到右指针=左指针，循环正常结束则输出True
    left = 0
    s = "".join( a.lower() for a in s if a.isalnum())
    right = len(s) -1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def isPalindrome_2(s: str):
    """
    :type s: str
    :rtype: bool
    """
    # 方法2： 字符串反转比较
    s = "".join( a.lower() for a in s if a.isalnum())

    return s == s[::-1]



s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
print(isPalindrome_2(s))