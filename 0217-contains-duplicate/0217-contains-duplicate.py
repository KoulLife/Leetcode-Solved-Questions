class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        newHash = set()
        for i in nums:
            if i in newHash:
                return True
            newHash.add(i)
        return False