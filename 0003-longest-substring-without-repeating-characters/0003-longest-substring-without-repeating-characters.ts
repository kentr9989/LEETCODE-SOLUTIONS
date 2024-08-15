function lengthOfLongestSubstring(s: string): number {
        // Implement new set char_set
        const charSet: Set<string> = new Set();
        
        // Initialize res equal to 0
        let res: number = 0
    
        // Initialize left pointer to 0
        let left: number = 0    
        
        // Iterate through the string with the right pointer
            // While the character on the right is in char_set
                // Remove the most left character from char_set
                // Increase the left pointer
            // Add the rightmost character to char_set
            // Update our res for the max substring length between res and (right - left + 1)
        
        for (let right = 0; right < s.length; right++) {
            while (charSet.has(s[right])) {
                charSet.delete(s[left]);
                left += 1;
            }
            charSet.add(s[right]);
            res = Math.max(res, (right - left + 1));
        }
        
        // Return res
        return res;
};