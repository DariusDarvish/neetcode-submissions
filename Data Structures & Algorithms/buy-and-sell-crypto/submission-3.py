class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price=prices[0]
        highest_profit=0
        for x in prices:
            lowest_price=min(x,lowest_price)
            highest_profit=max(highest_profit,x-lowest_price)
        return highest_profit