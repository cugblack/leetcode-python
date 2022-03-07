class Solution:
    """
    二维数组 对角线遍历
    共有m+n-1条对角线，从[0][0]开始遍历 m（行）次，再遍历n-1（列）次
    """
    def findDiagonalOrder(self, matrix):
        if not matrix:
            return False
        length_raw = len(matrix)
        length_column = len(matrix[0])
        res = []
        
        for l in range(length_raw + length_column -1):
            temp = [matrix[i][l-i] for i in range(max(0, l - length_column + 1), min(l + 1, length_raw))]
            res += temp if l % 2 == 1 else temp[::-1]
        return res
            
                