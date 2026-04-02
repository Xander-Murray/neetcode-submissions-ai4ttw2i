class Solution:
    def longestPalindrome(self, s: str) -> str:

        resLen = 0
        resIdx = 0

        def checkPalindrome(l,r):
            nonlocal resLen, resIdx
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    resIdx = l
                l -= 1
                r += 1




        for i in range(len(s)):
            checkPalindrome(i,i)
            checkPalindrome(i, i+ 1)

        return s[resIdx: resIdx + resLen]




        