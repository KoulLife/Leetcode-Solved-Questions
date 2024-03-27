class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        check = set()
        
        for i in arr:
            if i not in dic:
                dic[i] = 1
            elif i in dic:
                dic[i] += 1
        
        for j in dic:
            if dic[j] in check:
                return False
            check.add(dic[j])
        
        return True
        