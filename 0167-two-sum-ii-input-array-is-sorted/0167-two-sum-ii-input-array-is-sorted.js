/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    // Init left and right as 2 pointers
    let left = 0;
    let right = numbers.length -1;
    // while left > right
    //  sum = numbers[left] + numbers[right]
    //  if sum equal to target
    //     we can return [left + 1,right + 1]
    //  else if sum < target
    //     we can increase left poitner by 1
    //  else sum > target
    //     we can decrease right pointer by 1
    
    while (left < right) {
        const sum = numbers[left] + numbers[right];
        
        if (sum === target) {
            return [left + 1, right + 1];
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }
    
    // Time complexity : O(n)
    // Space complexity : O(1)
    
};