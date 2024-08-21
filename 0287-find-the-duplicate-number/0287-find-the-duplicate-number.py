class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0,0
        
        # keep going until they intersect
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]] # 2 move ahead
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            
            if slow == slow2:
                break
        return slow
        