class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] < prices[r]:
                p = prices[r] - prices[l]
                maximum = max(maximum, p)
            else:
                l = r
            r += 1
        return maximum