class Solution:
    def twoSum(self,nums: List[int], target: int) -> List[int]:
        # map the value of num by value
        nums_map = {}
        for index,num in enumerate(nums):
            nums_map[num] = index
        print(nums_map)
        # for each num, check if (target - num) is in nums_map
        for index,num in enumerate(nums):
            need_to_find = target - num
            if need_to_find in nums_map and index != nums_map[need_to_find]:
                return [index,nums_map[need_to_find]]
        return []
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         target_map = {}
#         for index,num in enumerate(nums):
#             target_map[num] = index
#         print(target_map)
#         for index,num in enumerate(nums):
#             find_value = target - num
#             if find_value in target_map:
#                 print(find_value)
#                 if index != target_map[find_value]:
#                     return [index, target_map[find_value]]
                
#         return []


# if __name__ == "__main__":
#     solution = Solution()
#     result = solution.twoSum([3, 2, 4], 6)
#     print(f"test: {result}")  # Expected output: [1, 2]



# class Solution:
#     # Time complexity: O(size of nums)
#     # Space complexity: O(size of nums)
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         # Create a dict map to store the value: index
#         map = {}
#         # for each index,num in nums:
#         #   cal find_value = num - target
#         #   if find_value in map:
#         #       return the [index,map[find_value]]
#         #   add num to map with its index
#         for index,num in enumerate(nums):
#             find_value = target - num
#             if find_value in map:
#                 return [index,map[find_value]]
#             map[num] = index
#         # return [] because no element found
#         return []
        
