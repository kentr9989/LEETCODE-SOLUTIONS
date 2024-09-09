class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Space complexity : O(size of nums)
        # Time complexity : O(size of nums)
        freq_count = {}
        for num in nums:
            if num in freq_count:
                return True
            freq_count[num] = True
        return False
        

    
    
        