class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       minPrice = prices[0]
       maxPrice = 0

       for price in prices[1:]:
        if price<minPrice:
            minPrice = price
        else:
            profit = price - minPrice
            maxPrice = max(maxPrice, profit)
       return maxPrice