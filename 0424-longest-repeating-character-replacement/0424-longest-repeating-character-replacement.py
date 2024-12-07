class Solution:
    # Space complexity : O(1) because only need to store 26 characters
    # Time complexity : Optimised O(n) not opt O(26n)
    def characterReplacement(self, s: str, k: int) -> int:
        # start with map with 26 characters key {key: characters, value: number of time occur}
        s.lower()
        map = {}
        
        # max_length = 0
        # Start with left and right at 0
        # while right < len(s):
        #   add the character s[right] to map
        #   curr_length = right - left + 1
        #   if curr_length - max_char in map < k:
        #       compare the curr_length and max_length
        #   else:
        #       if left < right:
        #           decrease s[left] from map
        #           increase left pointer by 1
        
        max_length = 0
        left, right = 0,0
        while right < len(s):
            if s[right] not in map:
                map[s[right]] = 0
            map[s[right]] += 1
            
            curr_length = right - left + 1
            curr_max_char = max(map.values())
            # print(f"map: {map}")
            # print(f"curr_length: {curr_length}")
            # print(f"curr_max_char: {curr_max_char}")
            if curr_length - curr_max_char <= k :
                max_length = max(max_length,curr_length)
            else:
                if left < right:
                    map[s[left]] -= 1
                    left += 1
            right += 1
        
        #  return max_length 
        return max_length
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         left = 0
#         char_set = {}
#         res = 0
#         for right in range(len(s)):
#             char_set[s[right]] = char_set.get(s[right],0) + 1
#             while (right - left + 1) - max(char_set.values()) > k:
#                 char_set[s[left]] -= 1
#                 left += 1
#             res = max(right - left + 1, res)
#         return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         char_count = {}
#         left = 0
#         res = 0
        
#         for right in range(len(s)):
#             char_count[s[right]] = char_count.get(s[right],0) + 1
#             while (right - left + 1) - max(char_count.values()) > k:
#                 char_count[s[left]] -= 1
#                 left += 1
#             res = max(res,(right - left + 1))
#         return res    
        
#         # init count_map {character : count}
#         count_map = {}
#         # int res 
#         res = 0
#         # init left = 0
#         left = 0
#         # for right(0) -> len(s)
#         #   plus 1 to count chracter of right
#         #   while window is not valid meaning
#         #   (r-l+1) - max(count.values()) > k:
#         #      decrement count of left 
#         #      increase left pointer by 1
#         #   update res between res and right - left + 1
#         for right in range(len(s)):
#             count_map[s[right]] = 1 + count_map.get(s[right],0)
#             while (right - left + 1) - max(count_map.values()) > k:
#                 count_map[s[left]] -= 1
#                 left += 1
#             res = max(res, (right - left + 1))    
            
#         # return res
#         return res
        