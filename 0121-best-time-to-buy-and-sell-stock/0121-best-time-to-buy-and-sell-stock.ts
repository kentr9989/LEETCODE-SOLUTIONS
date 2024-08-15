function maxProfit(prices: number[]): number {
        // Initialize left pointer at 0 (Buy)
        let left: number = 0;
    
        // Initialize right pointer at 1 (Sell)
        let right: number = 1;
    
        // Initialize max_profit to 0
        let maxProfit: number = 0;
        
        // While right is less than the length of prices
            // if prices[left] < prices[right]:
                // Calculate profit
                // Update max_profit
            // else:
                // Update left to be right
            // Move the right pointer by 1
        while (right < prices.length) {
            if (prices[right] > prices[left]) {
                const currentProfit = prices[right] - prices[left];
                maxProfit = Math.max(currentProfit,maxProfit);
            } else {
                left = right;
            }
            right += 1;
           
        }   
        
        // Return max_profit
        return maxProfit;
};