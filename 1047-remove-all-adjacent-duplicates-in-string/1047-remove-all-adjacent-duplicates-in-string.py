class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        if s == "":
            return ""
        
        arr = []
        for i in s:
            if arr == [] or arr[-1] != i:
                arr.append(i)
            else:
                arr.pop()
        return "".join(arr)
            