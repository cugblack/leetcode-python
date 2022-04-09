# 9. 回文数
# https://leetcode-cn.com/problems/palindrome-number/

def is_palindrome_1(self, x: int) -> bool:
    x = str(x)
    i = 0
    j = len(x) - 1
    while i < j:
        if x[i] == x[j]:
            i += 1
            j -= 1
        else:
            return False
    return True


def is_palindrome_2(self, x: int) -> bool:
    x = str(x)
    return x == x[::-1]
