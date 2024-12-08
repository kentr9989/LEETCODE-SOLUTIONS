class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n) - length of s
    def minWindow(self, s: str, t: str) -> str:
        # map_t string t by frequency
        map_t = {}
        for ct in t:
            if ct not in map_t:
                map_t[ct] = 0
            map_t[ct] += 1
        # print(f"map_t: {map_t}")
        
        # init map_s
        map_s = {}
        # init have, need = 0, length of map t
        have, need = 0, len(map_t)
        # print(f"need: {need}")
        # init smallest_length = float(infinity)
        smallest_length = float("infinity")
        res_pointer = [float("-infinity"),float("-infinity")]
        # left, right = 0,0
        left, right = 0,0
        # while right < len(s):
        #   if s[right] not in map_s:
        #       map_s[s[right]] = 0
        #   map_s[s[right]] += 1
        #   if s[right] in map_t: 
        #      if map_s[s[right]] == map_t[s[right]]
        #         have += 1
        #   while have == need:
        #       curr_length = right - left + 1
        #       smallest_length = min(curr_length,smallest_length)
        #       map_s[s[left]] -= 1
        #       if map_s[s[left]] in map_t:
        #           if map_s[s[left]] not equal map_t[s[left]]:
        #               have -= 1
        #       if left < right:
        #           left += 1
        #       
        
        while right < len(s):
            if s[right] not in map_s:
                # print("hi")
                map_s[s[right]] = 0
            map_s[s[right]] += 1
            if s[right] in map_t:
                if map_s[s[right]] == map_t[s[right]]:
                    have += 1
            # print(f"map_s: {map_s}")
            # print(f"have: {have}")
            while have == need:
                curr_length = right - left + 1
                if curr_length < smallest_length:
                    smallest_length = curr_length
                    res_pointer[0] = left
                    res_pointer[1] = right
                # print(f"map_s[s[left]]: {map_s[s[left]]}")
                map_s[s[left]] -= 1
                # if map_s[s[left]] < 0:
                #     map_s[s[left]] = 0
                if s[left] in map_t and map_s[s[left]] < map_t[s[left]]:
                        have -= 1
                # if left < right: 
                left += 1
            right += 1
        #  return smallest_length
        
        print(f"res_pointer[0]: {res_pointer[0]} res_pointer[1]: {res_pointer[1]}")
        if res_pointer[0] == float("-infinity"):
            return ""
        
        return s[res_pointer[0]:res_pointer[1] + 1]
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if t == "":
#             return ""
#         map_s = {}
#         map_t = {}
        
#         # fill up map_t frequency
#         for char_t in t:
#             map_t[char_t] = map_t.get(char_t,0) + 1
            
#         # print(f"map_t: {map_t}")
#         have,need = 0, len(map_t)
#         # print(f"need: {need}")
         
        
#         resLen = float("infinity")
#         res = [-1,-1]
#         l = 0
        
#         for r in range(len(s)):
#             map_s[s[r]] = map_s.get(s[r],0) + 1
#             if s[r] in map_t and map_s[s[r]] == map_t[s[r]]:
#                 have += 1
#             # print(f"have: {have}")
#             # print(f"map_s: {map_s}")    
#             # print(f"left: {l}")
#             while have == need:
#                 if resLen > r - l + 1:
#                     resLen = r - l + 1
#                     res = [l,r]
                
#                 map_s[s[l]] -= 1
#                 # if map_s[s[l]] == 0: 
#                 #     del map_s[s[l]]    
#                 if s[l] in map_t and map_t[s[l]] > map_s[s[l]]:
#                     have -= 1
#                 l += 1
# #                 print(f"resLen: {resLen}")
# #                 print(f"res: {res}")
        
#         if resLen == float("infinity"):
#             return ""
            
#         return s[res[0]:res[1] + 1]
        
        
        
