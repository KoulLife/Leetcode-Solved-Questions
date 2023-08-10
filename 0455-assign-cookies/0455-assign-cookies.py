class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        
        g_cur, s_cur = 0, 0
        while g_cur < len(g) and s_cur < len(s):
            if g[g_cur] <= s[s_cur]:
                res += 1
                g_cur += 1
                s_cur += 1
            
            elif g[g_cur] > s[s_cur]:
                s_cur += 1
        
        return res