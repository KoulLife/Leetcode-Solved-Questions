class Solution:
    def rob(self, nums: List[int]) -> int:        
        for i in range(0, 3):
            nums.append(0)
        
        for j in range(len(nums) - 4, -1, -1):
            nums[j] += max(nums[j + 2], nums[j + 3])
        return max(nums[0], nums[1])
        