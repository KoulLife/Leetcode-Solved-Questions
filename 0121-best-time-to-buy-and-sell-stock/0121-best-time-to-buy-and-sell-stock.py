class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1. l = 0, r = 1, res = 0 으로 초기화
        # 2. r이 l보다 작을 경우 l = r, r += 1
        # 3. max(기존, r - l) 로 비교
        
        l, r, res = 0, 1, 0
        
        while r <= len(prices) - 1:
            if prices[r] < prices[l]:
                l = r
                r += 1
            elif prices[r] >= prices[l]:
                res = max(res, prices[r] - prices[l])
                r += 1
        return res