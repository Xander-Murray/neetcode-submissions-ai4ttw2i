class Solution:
    def countSubstrings(self, s: str) -> int:
        resLen = 0
        resIdx = 0
        cnt = 0
        def checkPalindrome(l,r):
            nonlocal resLen, resIdx, cnt
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    resIdx = l
                l -= 1
                r += 1
                cnt += 1
                




        for i in range(len(s)):
            checkPalindrome(i,i)
            checkPalindrome(i, i+ 1)

        return cnt
