class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices: number[]): number {
        let lowestPrice=prices[0]
        let highestPrice=0
        for(let i=0;i<prices.length;i++){
            lowestPrice=Math.min(lowestPrice,prices[i])
            highestPrice=Math.max(prices[i]-lowestPrice,highestPrice)
        }
        return highestPrice
    }
}
