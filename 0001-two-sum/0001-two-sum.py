class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newDic = {}
        for i in range(0, len(nums)):
            if target - nums[i] in newDic:
                return [newDic[target - nums[i]], i]
            newDic[nums[i]] = i

