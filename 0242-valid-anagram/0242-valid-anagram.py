class Solution:
    def isAnagram(self, s: str, t: str) -> bool: 
        # Count map of string s
        map_s = {}
        for st in s:
            if st not in map_s:
                map_s[st] = 0
            map_s[st] += 1
        print(f"map_s line 7: {map_s}")
        # check for every character of t, if exist on s
        # if yes then delete that
        for st in t:
            if st not in map_s:
                return False
            map_s[st] -= 1
            if map_s[st] == 0 :
                del map_s[st]
            
        print(f"map_s line 15: {map_s}")
        if len(map_s) == 0:
            return True
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         count_s = {}
#         for str_s in s:
#             count_s[str_s] = count_s.get(str_s,0) + 1
#         # print(count_s)
        
#         for str_t in t:
#             if str_t not in count_s:
#                 return False
#             count_s[str_t] -= 1
#             print(count_s)
#             if count_s[str_t] <= 0:
#                 del count_s[str_t]
#         print(count_s)       
#         return len(count_s) == 0
#         # return True
    
# if __name__ == "main":
#     solution = Solution()
    
#     print(f"{solution.isAnagram('anagram','nagaram')}")




        
        
        