class Solution:
    def isValid(self, s: str) -> bool:
        map = {")":"(", "]":"[", "}":"{"}
        stack = []
        
        for i in s:
            if i not in map:
                stack.append(i)
                
            elif not stack or stack[-1] != map[i]:
                return False
            
            else: stack.pop()
        
        return not stack