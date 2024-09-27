class Solution:
    # Time complexity : O(n^2)
    # Space complexity : O(1)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for index,num in enumerate(nums):
            if index > 0 and nums[index - 1] == num:
                continue
            left, right = index + 1, len(nums) - 1
            while left < right:
                if num + nums[left] + nums[right] < 0:
                    left += 1
                elif num + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    res.append([num,nums[left],nums[right]])
                    left += 1
                    while nums[left] == nums[left -1] and right > left:
                        left += 1
        
        return res
            
        
        
        
        
        
        
        
#         res = []
#         nums.sort()
#         for index,value in enumerate(nums):
#             if index > 0 and value == nums[index-1]:
#                 continue
#             left, right = index + 1, len(nums) -1
#             while left < right:
#                 if value + nums[left] + nums[right] < 0:
#                     left += 1
#                 elif value + nums[left] + nums[right] > 0:
#                     right -= 1
#                 else:
#                     res.append([value,nums[left],nums[right]])
#                     left += 1
#                     while nums[left] == nums[left -1] and right > left:
#                         left += 1
#         return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # init list of list res
#         res = []
#         # sort the nums
#         nums.sort()
#         # iterate over each index and value of sort nums:
#         #   if index > 0 and value is equal to previous value:
#         #       continue to avoid dup
#         #   After this is now turn to 2 sum problem
#         #   init left pointer as index + 1
#         #   init right pointer as length of nums - 1
#         #   while left is less than right:
#         #       make a sum of 3 values
#         #       if sum < 0:
#         #           increase left pointer
#         #       else if sum > 0:
#         #           decrease right pointer
#         #       else:
#         #           append to res the 3 values
#         #           increase left pointer by 1
#         #           while nums[left] not equal nums[left -1]
#         #           and right > left :
#         #               increase left pointer
#         for index,value in enumerate(nums):
#             if index > 0 and value == nums[index -1]:
#                 continue
#             left = index + 1
#             right = len(nums) - 1
#             while left < right:
#                 sum = value + nums[left] + nums[right]
#                 if sum < 0:
#                     left += 1
#                 elif sum > 0:
#                     right -= 1
#                 else:
#                     res.append([value,nums[left],nums[right]])
#                     left += 1
#                     while nums[left] == nums[left -1] and right > left:
#                         left += 1
                    
#         #  return res
#         return res
        
        
        
        