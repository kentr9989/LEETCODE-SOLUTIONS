function longestConsecutive(nums: number[]): number {
        // Create new set
        const numSet: Set<number> = new Set(nums);
        // Init longest_streak
        let longestStreak: number = 0;

        // Loop through each num in nums
            // Check if it is not the start of the sequence
                // Init length equal 0
                // While (num + length) in the set
                // Update the longest_streak
        for (const num of nums) {
            if (!numSet.has(num - 1)) {
                let length: number = 0;
                while (numSet.has(num + length)) {
                    length += 1;
                }
                longestStreak = Math.max(length,longestStreak);
            } 
        }       

        // Return longest_streak
       return longestStreak;
};