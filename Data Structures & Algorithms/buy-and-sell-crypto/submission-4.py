class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell_price=0
        buy_price=prices[0]
        sale_value=0
        for price in prices:
            buy_price=min(price,buy_price)
            sell_price=max(sell_price,price-buy_price)
        return((sell_price+buy_price)-buy_price)
    