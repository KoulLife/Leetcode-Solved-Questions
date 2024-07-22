class Solution:
    def reverseWords(self, s: str) -> str:
        test = s.strip().split(' ')
        test.reverse()
        test = [item for item in test if item != '']
        return ' '.join(test)