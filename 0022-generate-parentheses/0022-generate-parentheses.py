class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(l, r, s):
            if (len(s) == n * 2):
                res.append(s)
                return
            if l < n:
                dfs(l + 1, r, s + "(")
            if l > r:
                dfs(l, r + 1, s + ")")
        
        dfs(0,0,"")
        return res