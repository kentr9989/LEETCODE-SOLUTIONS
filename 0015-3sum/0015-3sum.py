class Solution:
    # Time complexity : O(n^2)
    # Space complexity : O(1)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # init list of list res
        res = []
        # sort the nums
        nums.sort()
        print(nums)
        # iterate over each index and value of sort nums:
        #   if index > 0 and value is equal to previous value:
        #       continue to avoid dup
        #   After this is now turn to 2 sum problem
        #   init left pointer as index + 1
        #   init right pointer as length of nums - 1
        #   while left is less than right:
        #       make a sum of 3 values
        #       if sum < 0:
        #           increase left pointer
        #       else if sum > 0:
        #           decrease right pointer
        #       else:
        #           append to res the 3 values
        #           increase left pointer by 1
        #           while nums[left] not equal nums[left -1]
        #           and right > left :
        #               increase left pointer
        for index,value in enumerate(nums):
            if index > 0 and value == nums[index -1]:
                continue
            left = index + 1
            right = len(nums) - 1
            while left < right:
                sum = value + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    res.append([value,nums[left],nums[right]])
                    left += 1
                    while nums[left] == nums[left -1] and right > left:
                        left += 1
                    
        #  return res
        return res
        
        
        
        