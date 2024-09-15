class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left += 1
            elif nums[mid] > target:
                right -= 1
            else: 
                return mid
        return -1
        
#         # init left 0
#         left = 0
#         # init right last index
#         right = len(nums) - 1
#         # while left less than or equal to right:
#         #   mid equal to (left + right) // 2
#         #   if the value of mid index > target:
#         #       decrease the right to mid - 1
#         #   else if value of mid index < target:
#         #       increase left to mid + 1
#         #   else:
#         #       return m
#         while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] < target:
#                 left = mid + 1
#             elif nums[mid] > target:
#                 right = mid - 1
#             else:
#                 return mid
        
#         # return -1 - means not found
#         return -1