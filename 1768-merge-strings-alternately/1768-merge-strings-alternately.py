class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = len(word1)
        w2 = len(word2)
        length = min(w1, w2)
        res = ""
        
        for i in range(length):
            res += word1[i] + word2[i]
        if w1 == w2:
            return res
        elif w1 > w2:
            res += word1[length:]
        elif w1 < w2:
            res += word2[length:]
        return res