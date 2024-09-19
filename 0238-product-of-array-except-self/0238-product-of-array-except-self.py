class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        tmp = 1
        zCnt = 0
        
        if 0 in nums:
            target = 0
            for i in range(len(nums)):
                if nums[i] == 0:
                    zCnt += 1
                    target = i
                    if zCnt >= 2:
                        return res
                else:
                    tmp *= nums[i]
                
            res[target] = tmp
            return res
                
        else:
            for i in nums:
                tmp *= i
            for i in range(len(nums)):
                res[i] = tmp // nums[i]
            return res