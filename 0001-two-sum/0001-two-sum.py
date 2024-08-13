class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store value : index
        map = {}
        # Loop through array nums
        for i,num in enumerate(nums):
            # If the complement is in the dictionary, return the indices
            complement = target - num
            if complement in map:
                return [i,map[complement]]
            # Otherwise, add the number and its index to the dictionary
            map[num] = i
            
        # Return an empty list if no solution is found
        return []