class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        preArr = [0]
        preSum = 0
        
        for i in gain:
            preSum += i
            preArr.append(preSum)
        
        return max(preArr)
        