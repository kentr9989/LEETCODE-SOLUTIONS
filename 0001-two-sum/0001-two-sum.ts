function twoSum(nums: number[], target: number): number[] {
    // Create a hashmap to store value : index
       const map : Map<number,number> = new Map();
        
    // Loop through array nums
    // Find the complement through hashmap
    // If dont have then we set value : index
    // If have then return [index, complement-index]
       for (const i in nums) {
           const complement = target - nums[i]; 
           if (map.has(complement)) {
               return [map.get(complement)!, Number(i)];
           }
           map.set(nums[i],Number(i));
       } 
    // return - no solution is found
    return [];
    // Time complexity : O(n)
    // Space complexity : O(n)    
    
};