class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        
        bracketHash = {
            ")" : "(",
            "]" : "[",
            "}" : "{",
        }
        
        for i in s:
            if i == "(" or i == "{" or i == "[":
                arr.append(i)
            else:
                if arr == []:
                    return False
                elif arr[-1] != bracketHash[i]:
                    return False
                else:
                    arr.pop()
        if arr == []:
            return True
        else:
            return False
            