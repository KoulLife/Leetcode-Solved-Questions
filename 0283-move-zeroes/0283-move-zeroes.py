class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeroArr = []
        
        if len(nums) > 1:
            i = 0
            n = 0
            
            for i in range(len(nums)):
                if nums[i - n] == 0:
                    zeroArr.append(0)
                    nums.pop(i - n)
                    n += 1
        nums.extend(zeroArr)