/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    
    // If there is no element then return empty
    if( nums.length === 0) {
        return 0;
    }
    
   
    // Create a hashmap
    // Then store each element to hmap
    let mapCount = new Map();
    for(const num of nums) {
        mapCount.set(num,num);
    }
    console.log(mapCount)
    // Init longestStreak
    let longestStreak = 0;
    
    // Loop through each element from 0 to nums.length - 1
    // Check hashamp if there is NO currElement -1 (mean start of sequence)
    // then we start currStreak as 1; 
    // Then we continue checking if it has +1 then plus currNum + 1 
    // and currStreak + 1. Then we compare currStreak and longestStreak
    for(let i = 0; i < nums.length; i++) {
        
        if(!mapCount.has(nums[i] - 1)) {
            let currStreak = 1;
            let currElement = nums[i];
            
            while(mapCount.has(currElement + 1)) {
                currStreak++;
                currElement++;
            }
            longestStreak = Math.max(currStreak,longestStreak);
            
        }
    }
    
    // return longestStreak
    return longestStreak;
    
    // Time complexity : O(n)
    // Space complexity : O(n)
};