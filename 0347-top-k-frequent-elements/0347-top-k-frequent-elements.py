class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kArr = []
        firstDic = {}

        for i in nums:
            if i in firstDic:
                firstDic[i] += 1
            if i not in firstDic:
                firstDic[i] = 1
        
        for i in range(0, k):
            tmp =  max(firstDic, key = firstDic.get)
            kArr.append(tmp)
            del firstDic[tmp]
        
        return kArr  