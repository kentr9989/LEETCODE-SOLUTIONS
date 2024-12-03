class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n) - from the set
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0,0
        map_char = {}
        max_length = 0
        
        while r < len(s):
            # print(f"1{s[l:r]}")
            if s[r] not in map_char:
                map_char[s[r]] = True
                curr_length = r - l + 1
                print(f"1curr_length: {curr_length}")
                max_length = max(curr_length,max_length)
                r += 1
                print(f"1{s[l:r]}")
            else:
                while s[r] in map_char and l <= r:
                    del map_char[s[l]]
                    l += 1
                    print(f"l: {l}")
                    print(f"r: {r}")
                    print(f"s: {s[l:r]}")
                # l += 1
                curr_length = r - l + 1
                print(f"2curr_length: {curr_length}")
                max_length = max(curr_length,max_length)
                map_char[s[r]] = True
                print(f"2{s[l:r]}")
                r += 1

        return max_length
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         left, right = 0, 0
#         longest_substr = 0
#         char_set = set()
        
#         while right < len(s):
#             while s[right] in char_set:
#                 char_set.remove(s[left])
#                 left += 1
#             curr_substr = right - left + 1
#             longest_substr = max(curr_substr,longest_substr)
#             char_set.add(s[right])
#             right += 1
            
#         return longest_substr 
        
        
#         char_set = set()
        
#         left = 0
#         res = 0
        
#         for right in range(len(s)):
#             while s[right] in char_set:
#                 char_set.remove(s[left])
#                 left += 1
#             res = max((right - left + 1), res)
#             char_set.add(s[right])
#         return res
    
        
        
        
#         # implement new set char_set
#         char_set = set()
        
#         # init res equal 0
#         res = 0
#         # init left pointer 0
#         left = 0
        
#         # for right in range (len(s)):
#         #   while character on the right is in char_set
#         #      remove the most left character from char_set
#         #      increase the left pointer
#         #   add right most character to char_set
#         #   update our res for the max substring between res and (r-l+1)
#         for right in range(len(s)):
#             while s[right] in char_set:
#                 char_set.remove(s[left])
#                 left += 1
#             char_set.add(s[right])
#             res = max(res, (right - left + 1))
            
        
        
#         # return res
#         return res