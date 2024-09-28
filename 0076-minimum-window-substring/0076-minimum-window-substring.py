class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n) - length of s
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        map_s = {}
        map_t = {}
        
        # fill up map_t frequency
        for char_t in t:
            map_t[char_t] = map_t.get(char_t,0) + 1
            
        # print(f"map_t: {map_t}")
        have,need = 0, len(map_t)
        # print(f"need: {need}")
         
        
        resLen = float("infinity")
        res = [-1,-1]
        l = 0
        
        for r in range(len(s)):
            map_s[s[r]] = map_s.get(s[r],0) + 1
            if s[r] in map_t and map_s[s[r]] == map_t[s[r]]:
                have += 1
            # print(f"have: {have}")
            # print(f"map_s: {map_s}")    
            # print(f"left: {l}")
            while have == need:
                if resLen > r - l + 1:
                    resLen = r - l + 1
                    res = [l,r]
                
                map_s[s[l]] -= 1
                # if map_s[s[l]] == 0: 
                #     del map_s[s[l]]    
                if s[l] in map_t and map_t[s[l]] > map_s[s[l]]:
                    have -= 1
                l += 1
#                 print(f"resLen: {resLen}")
#                 print(f"res: {res}")
        
        if resLen == float("infinity"):
            return ""
            
        return s[res[0]:res[1] + 1]
        
        
        
        
#         if t == "":
#             return ""
#         map_s = {}
#         map_t = {}
        
#         for st in t:
#             map_t[st] = map_t.get(st,0) + 1
#         # print(map_t)
#         have, need = 0, len(map_t)
#         resLen = float("infinity")
#         res = [-1,-1]
#         left = 0
        
#         for right in range(len(s)):
#             map_s[s[right]] = map_s.get(s[right],0) + 1
#             # print("map_s is" + str(map_s))
#             if s[right] in map_t and map_s[s[right]] == map_t[s[right]]:
#                 # print("map_s is" + str(map_s))
#                 # print("have is" + str(have))
#                 have += 1
           
#             # print("have is" + str(have))
#             while have == need:
#                 if (right - left + 1) < resLen:
#                     res = [left,right]
#                     # print("res is" + str(res))
#                     resLen = right - left + 1
#                 map_s[s[left]] -= 1
#                 if s[left] in map_t and map_s[s[left]] < map_t[s[left]]:
#                     have -= 1
#                 # print("res is" + str(res))
#                 left += 1 
# #                 print(res)
               
                
#         if resLen != float("infinity"):
#             return s[res[0]:res[1] + 1]
#         else:
#             return ""

    
    
    