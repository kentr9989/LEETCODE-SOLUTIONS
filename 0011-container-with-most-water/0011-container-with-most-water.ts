function maxArea(height: number[]): number {
        // Initialize result
        let res: number = 0;
        // Initialize left pointer at 0
        let left: number = 0;
        // Initialize right pointer at the last index
        let right: number = height.length - 1;

        // While left is less than right
            // Calculate the area: (right-left) * Math.min(height[left],height[right])
            // Update result with the maximum of 
            // the current result and the new area
            // Move the pointers based on the heights
        while (left < right) {
            let area = (right - left) * Math.min(height[left],height[right]);
            res = Math.max(area,res);
            if (height[left] < height[right]) {
                left++;
            } else if (height[left] > height[right]) {
                right--;
            } else {
                right--;
            }
        } 

        // Return the maximum area found
        return res;
        
    
};