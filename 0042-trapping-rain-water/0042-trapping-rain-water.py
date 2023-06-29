class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        res = 0
        maxLeft, maxRight = height[left], height[right]
        
        while left < right:
            maxLeft = max(maxLeft, height[left])
            maxRight = max(maxRight, height[right])
            
            if maxLeft <= maxRight:
                res += maxLeft - height[left]
                left += 1
            else:
                res += maxRight - height[right]
                right -= 1
        
        return res