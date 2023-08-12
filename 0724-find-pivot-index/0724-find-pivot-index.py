class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        preSum = 0
        preArr = [0]
        
        for i in nums:
            preSum += i
            preArr.append(preSum)
        
        for j in range(1, len(nums) + 1, 1):
            if preArr[j - 1] == preArr[-1] - preArr[j]:
                return j - 1
        
        return -1