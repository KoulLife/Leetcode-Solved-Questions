class RecentCounter:

    def __init__(self):
        self.arr = []

    def ping(self, t: int) -> int:
        cnt = 0
        
        self.arr.append(t)
        
        for i in self.arr:
            if (t-3000) <= i <= t:
                cnt += 1
        return cnt

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)