class Solution:
    """
    给定两个二进制字符串，返回他们的和（用二进制表示）。
    输入为非空字符串且只包含数字 1 和 0。
    """
    def addBinary(self, a: str, b: str) -> str:
        if not a and not b:
            return []
        a = int(a, 2)
        b = int(b, 2)
        return bin(a+b)[2:]