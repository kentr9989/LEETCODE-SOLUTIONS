class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        # implement new set char_set
        char_set = set()
        
        # init res equal 0
        res = 0
        # init left pointer 0
        left = 0
        
        # for right in range (len(s)):
        #   while character on the right is in char_set
        #      remove the most left character from char_set
        #      increase the left pointer
        #   add right most character to char_set
        #   update our res for the max substring
        #   between res and (r-l+1)
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            res = max(res, (right - left + 1))
            
        
        
        # return res
        return res