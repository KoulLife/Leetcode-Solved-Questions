class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        tmp = 0
        arr = []
        
        for i in s:
            if i not in arr:
                arr.append(i)
                tmp = len(arr)
            else:
                res = max(res, tmp)
                idx = arr.index(i) + 1
                arr = arr[idx:]
                arr.append(i)
                tmp = len(arr)
        return max(res, tmp)
            