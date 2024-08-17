class Solution:
    # Time complexity: O(logn)
    # Space complexity: O(1)
    def findMin(self, nums: List[int]) -> int:
        # init left pointer first index of num
        left = 0
        # init right pointer last index of num
        right = len(nums) -1
        # init res = first element of nums
        res = nums[0]
        # while left less than or equal to right pointer:
        #   if nums at left < nums at right (in sort section):
        #       update the res with nums at left
        #       break for loop
        #   calculate mid posititon
        #   update the res with nums at mid
        #   if nums at mid >= nums at left:
        #       move the left pointer to mid + 1
        #   else:
        #       move the right pointer to mid - 1
        
        # return res
        
        while left <= right:
            if nums[left] < nums[right]:
                res = min(res,nums[left])
                break
            mid = (left + right) // 2
            print(mid)
            res = min(res,nums[mid])
            
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        return res