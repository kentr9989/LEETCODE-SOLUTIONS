class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(path):
            if len(path) == len(nums):
                res.append(path.copy())  # Use .copy() to avoid reference issues
                return
            
            for i in range(len(nums)):
                if nums[i] in path:  # Skip if already included in the current path
                    continue
                
                # Include the number in the current path
                path.append(nums[i])
                dfs(path)  # Recursive call
                path.pop()  # Backtrack to explore the next number

        dfs([])  # Start the recursion with an empty path
        return res
      