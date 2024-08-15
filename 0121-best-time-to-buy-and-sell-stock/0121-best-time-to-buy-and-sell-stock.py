class Solution:
    # Time complexity: 
    def maxProfit(self, prices: List[int]) -> int:
        # init left pointer 0 (Buy)
        left = 0
        # init right pointer 1 (Sell)
        right = 1
        # init max_profit = 0
        max_profit = 0
        
        # while right < length of prices
        #   if price[left] < price[right]:
        #       calc profit
        #       update the max_profit
        #   else:
        #       update the left to the right
        #   update the right pointer by 1
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit,profit)
            else:
                left = right
            right += 1
        
        #  return max_profit
        return max_profit