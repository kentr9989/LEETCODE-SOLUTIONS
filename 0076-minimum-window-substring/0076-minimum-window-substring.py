class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n) - length of s
    def minWindow(self, s: str, t: str) -> str:
        # if t is empty string:
        #   return the empty string
        if t == "": 
            return ""
        
        # init map for s {character : count}
        map_s = {}
        # init map for t {character : count}
        map_t = {}
        # inject all value for map t
        for char in t:
            map_t[char] = 1 + map_t.get(char,0)
        
        # init have is equal 0
        have = 0
        # init need as length of t
        need = len(map_t)
        # init res to be start and end index
        res = [-1,-1]
        # init res length to be infinity
        resLen = float("infinity")
        # init left pointer equal 0
        left = 0
        # for right pointer (0 -> length of s):
        #   add the character of s[right] to map of s
        #   check if s[right] is in map of t AND
        #   s[right] equal to map_t[s[right]]:
        #       increase have by 1
        #   while have == need:
        #       Update the new res and resLen
        #       remove s[left] from map_s
        #       check if s[left] is in map_t[] AND
        #       map_s[s[left]] < map_t[s[left]]:
        #           decrease have by 1
        #       increase left pointer by 1
        for right in range(len(s)):
            map_s[s[right]] = 1 + map_s.get(s[right],0)
            
            if s[right] in map_t and map_s[s[right]] == map_t[s[right]]:
                have += 1
                
            while have == need:
                if (right - left + 1) < resLen:
                    res = [left,right]
                    resLen = right - left + 1
                map_s[s[left]] -= 1
                if s[left] in map_t and map_s[s[left]] < map_t[s[left]]:
                    have -= 1
                left += 1
        
        # res = [left,right]    
        #  if resLen is still infinity:
        #       return "" - nothing is found
        #  else:
        #       return the string from pos left to right + 1 (slicing)
        if resLen != float("infinity"):
            return s[res[0]:res[1]+1]
        else:
            return ""
       
    
    
    
    
    