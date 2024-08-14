class Solution:
    # Time complexity : O(n) - max visit for each number is twice
    # Space complexity : O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        # Create new set
        num_set = set(nums)
        # Init longest_streak
        longest_streak = 0
        
        # Loop through each num in nums :
        #   check if it not the start of sequence (num - 1) not in set:
        #       initialise length equal 0
        #       while (n + length) in the set:
        #           increase length
        #       update the longest_streak
        for num in nums:
            if (num - 1) not in num_set: #start of sequence
                length = 0
                while (num+length) in num_set:
                    length += 1
                longest_streak = max(length,longest_streak)
        
        # return longest_streak
        return longest_streak
    
    
# Test case 1: Regular case
# print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))
# Output: 4

# Test case 2: Single element
# print(solution.longestConsecutive([1]))  
# Output: 1

# Test case 3: Empty list
# print(solution.longestConsecutive([]))  
# Output: 0

# Test case 4: All elements are the same
# print(solution.longestConsecutive([1, 1, 1, 1]))  
# Output: 1

# Test case 5: Long sequence
# print(solution.longestConsecutive([10, 5, 12, 3, 55, 30, 4, 2]))  # Output: 4 (sequence: 2, 3, 4, 5)

# Test case 6: Negative and positive numbers
# print(solution.longestConsecutive([-1, -2, 0, 1, 2, -3, 3, 4]))  # Output: 8 (sequence: -3, -2, -1, 0, 1, 2, 3, 4)