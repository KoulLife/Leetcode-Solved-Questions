class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        newHash = set()
        for i in s:
            if i not in newHash:
                newHash.add(i)
        
        for i in newHash:
            if s.count(i) != t.count(i):
                return False
        
        return True