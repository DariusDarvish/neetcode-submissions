class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest_price=prices[0]
        biggest_profit=0
        for x in prices:
            smallest_price=min(x,smallest_price)
            biggest_profit=max(biggest_profit,x-smallest_price)
        return biggest_profit