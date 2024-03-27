class Solution:
    def removeStars(self, s: str) -> str:
        arr = []
        for i in s:
            if(i != "*"):
                arr.append(i)
            elif(i == "*"):
                arr.pop()
        
        result = "".join(arr)
        
        return result