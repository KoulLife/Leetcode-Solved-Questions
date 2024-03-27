class RecentCounter:

    def __init__(self):
        self.queue = []
        self.res = 0

    def ping(self, t: int) -> int:
        if not self.queue:
            self.queue.append(t)
            self.res = 1
            return self.res
        else:
            self.queue.append(t)
            self.res = len(self.queue)
            while self.queue[0] < (t - 3000):
                self.res -= 1
                self.queue.pop(0)
            return self.res
                
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)