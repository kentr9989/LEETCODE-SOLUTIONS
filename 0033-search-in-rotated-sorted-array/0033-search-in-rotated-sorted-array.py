class Solution:
    def search(self, nums: List[int], target: int) -> int:
         # init left pointer first index of num
         left = 0
         # init right pointer last index of num
         right = len(nums) - 1
         res = -1
         # while left is less than equal or equal to right pointer:
         #      calc middle value
         #      if target equal nums at middle:
         #          return mid
         #      determine which portion we in
         #      if nums[l] <= nums[mid]: (we are in left point portion of array)
         #          if target > nums[mid] or target < nums[l]:
         #              left = mid + 1 (search the right portion)
         #          else:
         #              right = mid - 1 (search the left portion)
         #      else: (we are in right porition of array):
         #          if target < nums[mid] or target > nums[r]:
         #              right = mid - 1 (search the left portion)
         #          else:
         #              left = mid + 1 (search the right portion)
         while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] >= nums[left]:
                    if target > nums[mid] or target < nums[left]:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    if target < nums[mid] or target > nums[right]:
                        right = mid - 1
                    else:
                        left = mid + 1
            
         # return res   
         return -1
        
        