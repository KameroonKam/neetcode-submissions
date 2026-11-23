class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        l, r = 0, 1 #left = buy, right = sell
        maxP = 0 
        while r < len(prices):
            if prices[l] < prices[r]:
                diff = prices[r] - prices[l]
                maxP = max(diff, maxP)
                r += 1
            else:
                l = r 
                r += 1 

        return maxP