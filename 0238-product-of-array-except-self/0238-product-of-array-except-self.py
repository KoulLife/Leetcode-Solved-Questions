class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        newHash = {}
        sum = 1
        zeroNum = 0
        
        for i in range(0, len(nums)):
            newHash[i] = nums[i]
            if nums[i] == 0:
                zeroNum += 1
            else:
                sum = sum * nums[i]
        
        if zeroNum == 1:
            for k in range(0, len(nums)):
                if nums[k] == 0:
                    res[k] = sum
                else:
                    res[k] = 0
        
        elif zeroNum > 1:
            for l in range(0, len(nums)):
                res[l] = 0
        
        else:
            for j in range(0, len(nums)):
                res[j] = sum // newHash[j]
            
        
        return res