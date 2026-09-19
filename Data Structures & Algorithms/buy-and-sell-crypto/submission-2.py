class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest_price=prices[0]
        biggest_profit=0
        for price in prices:
            smallest_price=min(smallest_price,price)
            biggest_profit=max(biggest_profit,price-smallest_price)
        return biggest_profit