function characterReplacement(s: string, k: number): number {
        // Initialize count_map {character : count}
        const countMap: Map<string,number> = new Map();
        // Initialize result
        let res: number = 0;
        // Initialize left pointer to 0
        let left: number = 0;

        // Helper function to get the maximum value from the count map
        const getMaxCount = (countMap: Map<string,number> ): number => {
            let maxCount: number = 0;
            for (const [character,count] of countMap) {
                maxCount = Math.max(maxCount,count);
            }
            return maxCount;
        }

        // Iterate through the string with the right pointer
            // Increase the count of the character at the right pointer
            // While the window is not valid
                // Decrease the count of the character at the left pointer
                // Increase the left pointer
            // Update the result with the maximum value between res and the current window size
        for (let right = 0; right < s.length; right++) {
            countMap.set(s[right],1 + (countMap.get(s[right]) || 0));
            while ((right - left + 1) - getMaxCount(countMap) > k) {
                countMap.set(s[left],countMap.get(s[left]) -1);
                left += 1;
            }
            res = Math.max((right - left + 1),res);
        }
        
        // Return the result
        return res;
       
};