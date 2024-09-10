class Solution:
    # Time complexity: O(length of s + length of t) 
    # Space complexity: O(length of s)
    def isAnagram(self, s: str, t: str) -> bool:
        # if the length of s not equal length of t:
        #   return False
        if len(s) != len(t):
            return False
        # Create the map to count the freq_count_s of s
        freq_count_s = {}
        # Map all the character of s to freq_count_s
        for char in s:
            freq_count_s[char] = freq_count_s.get(char,0) + 1
            
        # For each character char of t
        # If char is not in freq_count_s:
        #   return False
        # reduce the freq_count_s[char] by 1
        # if freq_count_s[char] is equal 0:
        #   delete freq_count_s[char]
        for char in t:
            if char not in freq_count_s:
                return False
            freq_count_s[char] -= 1
            if freq_count_s[char] == 0:
                del freq_count_s[char]
        
        
        # return true if length of freq_count_s is 0 else false
        return len(freq_count_s) == 0
        
        
        
        