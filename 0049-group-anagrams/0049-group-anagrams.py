class Solution:
    # n : number of strings
    # k : avg length of each string
    # Time complexity: O(nlogk)
    # Space complexity: O(nk)
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
        

        

        