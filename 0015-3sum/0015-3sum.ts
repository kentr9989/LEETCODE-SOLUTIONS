function threeSum(nums: number[]): number[][] {
        // Init list of lists res
        const res: number[][] = [];
        // Sort the nums
        nums.sort((a,b) => a-b);

        // Iterate over each index and value of sorted nums
            // If index > 0 and value is equal to previous value, 
            //continue to avoid dup
            // After this it is now turned to 2 sum problem
            // Init left pointer as index + 1
            // Init right pointer as length of nums - 1
            // While left is less than right
            //       make a sum of 3 values
            //       if sum < 0:
            //            increase left pointer
            //       else if sum > 0:
            //            decrease right pointer
            //       else:
            //           append to res the 3 values
            //           increase left pointer by 1
            //           while nums[left] not equal nums[left -1]
            //           and right > left :
            //               increase left pointer
        for (const [index,value] of nums.entries()) {
            if (index > 0 && value == nums[index -1]) continue;
            let left: number = index + 1;
            let right: number = nums.length - 1;
            while (left < right) {
                const sum: number = value + nums[left] + nums[right];
                if (sum < 0) {
                    left += 1;
                } else if (sum > 0) {
                    right -= 1;
                } else {
                    res.push([value,nums[left],nums[right]]);
                    left += 1;
                    while (nums[left] == nums[left -1] &&
                           left < right 
                          ) {
                            left += 1;
                    }
                }
            }
        }
            

        // Return res
        return res;
        
};