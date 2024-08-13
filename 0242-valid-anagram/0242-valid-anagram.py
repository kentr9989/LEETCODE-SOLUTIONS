class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # if length s not equal t return false
        if len(s) != len(t):
            return False;
        
        # make a dictionary to store character counts
        firstMapCount = {}

        # store dictionary with char counts from s
        for char in s:
            firstMapCount[char] = firstMapCount.get(char,0) + 1
        
        
        # for each char in t check the following
        for char in t:
            if char not in firstMapCount:
                return False
            
            firstMapCount[char] -= 1
            if firstMapCount.get(char) == 0:
                del firstMapCount[char]
        
        # return true because the dictionary contains both s and t
        return len(firstMapCount) == 0
        
        