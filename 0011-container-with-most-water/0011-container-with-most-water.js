/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    // Init left and right pointer
    // Init maxArea to be 0
    let left = 0;
    let right = height.length - 1;
    let maxArea = 0;
    
    // while left < right :
    //  width is right - left
    //  height is min max height[left] and height[right]
    //  currentArea = width * height
    //  Compare current maxArea with currentArea
    //  Exp: We shift the lower height 
    //  while(height[left] < height[right]):
    //      left++;
    //  else:
    //      right--
    
    while(left < right) {
        const width = right - left;
        const currHeight = Math.min(height[left],height[right]);
        const currentArea = width * currHeight;
        
        maxArea = Math.max(currentArea,maxArea);
        
        if(height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }
    
    //return maxArea;
    return maxArea;
    
    // Time complexity : O(n)
    // Space complexity : O(1)
};