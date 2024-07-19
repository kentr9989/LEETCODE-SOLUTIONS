/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    // Create a hashmap to store value : index
    let map = new Map();
    
    // Loop through array nums
    // Find the complement through hashmap
    // If dont have then we set value : index
    // If have then return [index, complement-index]
    for(let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        
        if(map.has(complement)) {
            return [map.get(complement),i];
        }
        map.set(nums[i],i);
    }
    
    // return - no solution is found
    return;
        
    // Time complexity : O(n)
    // Space complexity : O(n)    
    
};