class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        

        for i in range(len(prices) - 1, 0, -1):
            if prices[i] - min(prices[:i]) > maximum:
                maximum = prices[i] - min(prices[:i])
        return maximum