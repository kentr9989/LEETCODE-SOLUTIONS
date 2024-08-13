class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create new dictionary : (sortedStr, value)
        anagram_map = {}

        # For each element in strs:
        #    sort the element
        #    if sorted_element in map:
        #      add element to the value
        #    else:
        #      add sorted_element to map
        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str not in anagram_map:
                anagram_map[sorted_str] = []
            anagram_map[sorted_str].append(str)
        
        # return the values in the map
        return list(anagram_map.values())
    
    
    
    # Time complexity : O(n * klogk) where k is length for each         string
    # Space complexity: O(n*k)

        