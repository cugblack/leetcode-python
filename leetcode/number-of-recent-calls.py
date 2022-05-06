# 933. 最近的请求次数
# https://leetcode-cn.com/problems/number-of-recent-calls/

class RecentCounter:
    def __init__(self, l=[]):
        self.l = []

    def ping(self, t: int) -> int:
        self.l.append(t)
        while self.l[0] < t-3000:
            self.l.pop(0)
        return len(self.l)

# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
print(obj.ping(1))
print(obj.ping(100))
print(obj.ping(101))
print(obj.ping(10001))
