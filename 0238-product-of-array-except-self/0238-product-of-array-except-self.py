class Solution:
    # Time complexity : O(n)
    # Space complexity : O(1)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        prefix = 1
        for index,num in enumerate(nums):
            res[index] = prefix
            prefix *= num
        print(res)
        
        postfix = 1
        # res2 = [1] * len(nums)
        for index in range(len(nums) - 1, -1, -1):
            res[index] *= postfix
            postfix *= nums[index]
        # print(res2)    
        return res
        
        
        
#         # create res array
#         res = [1] * len(nums)
        
#         prefix = 1
#         for index,num in enumerate(nums):
#             res[index] = prefix
#             prefix *= num
            
#         postfix = 1
#         for i in range(len(nums) -1 , -1,-1):
#             res[i] *= postfix
#             postfix *= nums[i]
        
#         return res
        
        
#-------------------------------------------------------------------------        
        # # Create res array
        # res = [1] * (len(nums))
        # # init prefix 1
        # # for each pos of res (0 -> num-1)
        # #     put the prefix in the position of res[i]
        # #     update the prefix by prefix *= nums[i]
        # prefix = 1
        # for i in range(len(nums)):
        #     res[i]  = prefix
        #     prefix *= nums[i]
        # # init postfix 1
        # # for each post of res (num-1 -> 0)
        # #     update res[i] *= postfix
        # #     update postfix  by *= nums[i]  
        # postfix = 1
        # for i in range(len(nums)-1,-1,-1):
        #     res[i] *= postfix
        #     postfix *= nums[i]
        # #return res
        # return res