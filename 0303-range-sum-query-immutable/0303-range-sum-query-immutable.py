class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        tmp = 0
        self.prefix.append(tmp)
        for i in nums:
            tmp += i
            self.prefix.append(tmp)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)