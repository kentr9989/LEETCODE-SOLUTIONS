/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    // Init res
    // Init left and right pointer
    let res = nums[0];
    let left = 0;
    let right = nums.length - 1;
    
    // while left <= right:
    //  EXP: If the subarray is already sorted, update the result and break
    //  if nums[left] < nums[right] :
    //      res is min between res and nums[left]
    //      break out of the loop
    //  calculate mid as Math.floor of left + right / 2
    //  EXP: Determine which side to search on because of the rotation
    //       If nums[mid] >= nums[left] means the smaller half is on the right side
    //       otherwise the smaller half is on the left side
    //  if nums[mid] >= nums[left]:
    //      left = mid + 1;
    //  else :
    //      right = mid - 1;
    
    while (left <= right) {
        if (nums[left] < nums[right]) {
            res = Math.min(res,nums[left]);
            break;
        }
        
        let mid = Math.floor((left + right)/2);
        res = Math.min(res,nums[mid]);
        if (nums[mid] >= nums[left]) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
        
    }
    
    // return res
    return res;
    // Time complexity : O(n) because each iteration of binary search reduces search by half
    // Space complexity : O(1) because we use constant amount of space 
};