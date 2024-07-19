/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    
    // Create an array of answer
    let answer = new Array(nums.length).fill(1);
    
    // Compute the prefix (from 0 -> nums.length - 1)
    // Start with prefix = 1 go from left -> right
    // answer[i] *= prefix then prefix *= nums[i]
    let prefix = 1;
    for(let i = 0; i < nums.length; i++) {
        answer[i] *= prefix;
        prefix *= nums[i];
    }
    
    // Compute the suffix (from nums.length - 1 -> 0)
    // Start with suffix = 1 go from right -> left
    // answer[i] *= suffix then suffix *= nums[i]
    let suffix = 1;
    for(let i = nums.length - 1; i >= 0; i--) {
        answer[i] *= suffix;
        suffix *= nums[i];
    }
    
    return answer;
};