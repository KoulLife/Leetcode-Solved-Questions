class MinStack:

    def __init__(self):
        self.st = []

    def push(self, x: int) -> None:
        currMin = self.getMin()
        if currMin == None or x < currMin:
            currMin = x
        self.st.append([x, currMin])

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        if len(self.st) == 0:
            return None
        return self.st[len(self.st) -1][0]

    def getMin(self) -> int:
        if len(self.st) == 0:
            return None
        return self.st[len(self.st) -1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()