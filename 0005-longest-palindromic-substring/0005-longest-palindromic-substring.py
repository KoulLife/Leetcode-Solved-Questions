class Solution(object):
    def longestPalindrome(self, s):
        def slide(left, right):
            while left>=0 and right<len(s) and s[left] == s[right]:
            # 왼쪽과 오른쪽이 같으면 팰린드롬
                left-=1
                right+=1
            return s[left+1:right]

        if len(s) == 1 or s == s[::-1]:
        # 문자열 길이가 1 이거나 문자열 전체가 팰린드롬이면 바로 리턴 (최적화)
            return s

        ans = ""

        for i in range(len(s)-1):
            ans = max(ans, slide(i,i), slide(i,i+1), key = len)
            # 길이가 짝수인 팰린드롬도 있을 수 있으니 i, i+1 도 추가
        return ans
