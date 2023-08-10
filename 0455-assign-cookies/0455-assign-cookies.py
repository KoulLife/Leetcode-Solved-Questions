class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        cnt = 0
        g_left, s_left = 0, 0
        
        while g_left < len(g) and s_left < len(s):
            if g[g_left] <= s[s_left]:
                cnt += 1
                g_left += 1
                s_left += 1
            
            elif g[g_left] > s[s_left]:
                s_left += 1
        
        return(cnt)