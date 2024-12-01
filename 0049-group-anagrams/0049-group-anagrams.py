class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map : {key : sorted_str , value: array of original value}
        map = {}
        res_arr = []
        
        # push into map according to sorted str
        for st in strs:
            sorted_str = ''.join(sorted(st))
            # print(f"sorted_str {sorted_str}")
            if sorted_str not in map:
                map[sorted_str] = []
            map[sorted_str].append(st)
        
        for items,values in map.items():
            res_arr.append(values)
        # print(map)
            
            
        return res_arr
        
        
        
        
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            #     # Time complexity : O(length of strs * length of each str * log(length of each str))
#     # Space complexity: O(length of strs * length of each str)
        
#         # make a map {key : sorted , value : array of original str}
#         map = {}
#         for str in strs:
#             sort_str = ''.join(sorted(str))
#             if sort_str not in map:
#                 map[sort_str] = []
#             map[sort_str].append(str)
#         print(map)
#         return list(map.values())
        
# if __name__ == "__main__":
#     solution = Solution()
#     result = solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
#     print(f" Result: {result}")




# class Solution:
#     # Time complexity : O(length of strs * length of each str * log(length of each str))
#     # Space complexity: O(length of strs * length of each str)
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         # Create a map to store sortedStr : array of real value
#         map = {}
#         # For each str in strs:
#         #   sort the str by alphabetical order
#         #   if the sort str is not in map:
#         #       add the sort string to the map as key and value is []
#         #   else:
#         #       add the str (NOT SORTED) to the map value
#         for str in strs:
#             sort_str = ''.join(sorted(str))
#             if sort_str not in map:
#                 map[sort_str] = []
#             map[sort_str].append(str)
        
#         # return the array from value from map
#         return list(map.values())
        

        