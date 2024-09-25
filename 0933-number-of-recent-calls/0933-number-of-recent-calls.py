class RecentCounter:

    def __init__(self):
        self.dq = []

    def ping(self, t: int) -> int:
        if self.dq == []:
            self.dq.append(t)
            return 1
        
        n = 0
        
        for i in range(len(self.dq)):
            if self.dq[i] < t - 3000:
                n += 1
            else:
                break
        if n >= 1:
            for _ in range(n):
                self.dq.pop(0)
        self.dq.append(t)
        return len(self.dq)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)