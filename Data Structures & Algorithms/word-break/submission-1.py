class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        
        maxLen = 0
        minLen = float("inf")

        for w in wordDict:
            maxLen = max(maxLen, len(w))
            minLen = min(minLen, len(w))

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(max(0, i - maxLen), i - minLen + 1):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break

        return dp[len(s)]