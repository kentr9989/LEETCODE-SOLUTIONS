/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    // Init left = 0 - buy day
    // Init right = 1 - sell day
    // Init maxP = 0
    let left = 0;
    let right = 1;
    let maxP = 0;
    
    // while right < prices.length
    //  if prices[left] < prices[right]:
    //      currP = prices[right] - prices[left]
    //      Get the latest maxP
    //  else:
    //      EXP: shift the latest left same as right
    //           because we want the lowest price possibile
    //      left = right
    //  right++
    
    while(right < prices.length) {
        if(prices[left] < prices[right]) {
            let currentP = prices[right] - prices[left];
             maxP = Math.max(currentP,maxP);
        } else {
            left = right;
        }
        right++;
       
    }
     
    // return maxP
    return maxP;
    
    // Time complexity : O(n)
    // Space complexity : O(1)
 };