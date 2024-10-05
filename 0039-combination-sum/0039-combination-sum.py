class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        
        def dfs(i,curr,total):
            if total == target:
                res.append(copy.copy(curr))
                return
            if i >= len(candidates) or total > target:
                return
           
            # decision to include nums[i] and go ahead with it
            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])
            
            # decision not to include nums[i]
            curr.pop()
            dfs(i + 1, curr, total)
        
        dfs(0,curr,0)
        return res
    # res = []
    # curr = [2,3,6]
    # dfs(0,curr,0)
    #    dfs(1,[2],2)
    #      dfs(2,[2,3],5)
            
    
    
    