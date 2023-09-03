class Solution:
    def climbStairs(self, n: int) -> int:
        cashe = [0] * 46
        cashe[1] = 1
        cashe[2] = 2
        
        for i in range(3, n + 1):
            cashe[i] = cashe[i - 1] + cashe[i - 2]
        
        return(cashe[n])