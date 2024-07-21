/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    // Sort the array in increasing order
    nums.sort((a,b) => a - b);
    
    // Init the res array
    const res = [];
    
    
    // Init for loop from i = 0 to i = nums.length - 2 (to save enough space for 2 pointers left and right)
    //    If i > 0 AND currentElement === nextElement then continue looping (because triplets have distict element and skip dulicate)
    //    Init left = i + 1 and right = num.length - 1  
    //    while(left < right)
    //        Init currentSum 
    //        if currentSum equals to 0
    //           push all 3 elements to the res array
    //        else if currentSum < 0 
    //           increase left pointer
    //        else
    //           decrease right pointer
    
    for(let i = 0; i < nums.length - 2; i++) {
        // Skip duplicate for first element
        if (i > 0 && nums[i] === nums[i-1]) continue;
        
        let left = i + 1;
        let right = nums.length - 1;

        while (left < right) {
            const currentSum = nums[i] + nums[left] + nums[right];
            if (currentSum === 0) {
                res.push([nums[i],nums[left],nums[right]]);
                
                // Skip duplicates for the second and third elements
                while (left < right && nums[left] === nums[left + 1]) left++;
                while (left < right && nums[right] === nums[right - 1]) right--;
                
                left++;
                right--;
            } else if (currentSum < 0) {
                left++;
            } else {
                right--;
            }
        }
    }
    // return res array
    return res;
    
    // Time complexity : O(n^2)
    // Space complexity : O(1) or O(n) - depending sort library
};