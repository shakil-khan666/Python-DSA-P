from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float("inf")
        for price in prices:
            min_price = min(min_price,price)
            sell_price = price-min_price
            max_profit = max(sell_price,max_profit)
        return max_profit
    

number = [7,1,6,4,3,2]
s=Solution()
print(s.maxProfit(number))
    
            
            