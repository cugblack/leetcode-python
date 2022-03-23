# 1217. 玩筹码
# https://leetcode-cn.com/problems/minimum-cost-to-move-chips-to-the-same-position/
# 给你一个数组
#   下标表示第 i 个筹码
#   值表示这个筹码的所在位置
# 你的任务是，把所有筹码挪到相同的位置，计算最小移动的步数
#   移动偶数步不消耗步数，移动奇数步，消耗一步
#   所以为了最小化步数，我们先尽量使步数为0,也就是先偶数地挪动。
#   我们可以把在偶数位的都挪到一起，把在奇数位的都挪到一起。
#   这样，只要比较哪个多，把剩下的都挪过去即可。
#   所以这道题目实际上就是让你计算一个数列中奇数和偶数的数量的最小值。


def minCostToMoveChips(self, position):
    """
    :type position: List[int]
    :rtype: int
    """
    odd = sum(1 for i in position if i % 2 == 0)
    return min(odd, len(position) - odd)

position = [2, 2, 2, 3, 3]

print(minCostToMoveChips(position))