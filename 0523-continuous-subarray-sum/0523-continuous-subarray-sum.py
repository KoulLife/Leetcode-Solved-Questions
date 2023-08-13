class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        preSum = [0]
        Sum = 0
        for i in range(len(nums)):
            Sum += nums[i]
            preSum.append(Sum)
        Dict = {}

        for i in range(len(preSum)):
            r = preSum[i] % k
            if r not in Dict:
                Dict[r] = i
            else:
                if i - Dict[r] >= 2:
                    return True

        return False
