class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                curr_profit = prices[r] - prices[l]
                max_profit = max(curr_profit,max_profit)
                r += 1
            else:
                l = r
                r += 1
        
        
        return max_profit
        
        
        
        
        
        
        
        
        
        
        
#         max_profit = 0
#         left , right = 0, 1
#         while right < len(prices):
#             if prices[left] < prices[right]:
#                 curr_profit = prices[right] - prices[left]
#                 print(f"curr profit: {curr_profit}")
#                 max_profit = max(max_profit, curr_profit)
#             else:
#                 left = right
#             right += 1
        
        
#         return max_profit

        
        
        
        
        
        
        
        # left = 0
        # right = 1
        # max_profit = 0
        # while right < len(prices):
        #     if prices[left] < prices[right]:
        #         profit = prices[right] - prices[left]
        #         max_profit = max(max_profit,profit)
        #     else:
        #         left = right
        #     right += 1
        # return max_profit
            
        
        
#         # init left pointer 0 (Buy)
#         left = 0
#         # init right pointer 1 (Sell)
#         right = 1
#         # init max_profit = 0
#         max_profit = 0
        
#         # while right < length of prices
#         #   if price[left] < price[right]:
#         #       calc profit
#         #       update the max_profit
#         #   else:
#         #       update the left to the right
#         #   update the right pointer by 1
#         while right < len(prices):
#             if prices[left] < prices[right]:
#                 profit = prices[right] - prices[left]
#                 max_profit = max(max_profit,profit)
#             else:
#                 left = right
#             right += 1
        
#         #  return max_profit
#         return max_profit