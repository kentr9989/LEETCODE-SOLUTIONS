class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_map = {}
        s2_map = {}
        
        # Map s1_map and s2_map by same index of s1
        for i in range(len(s1)):
            s1_map[s1[i]] = s1_map.get(s1[i], 0) + 1
            s2_map[s2[i]] = s2_map.get(s2[i], 0) + 1
        
        # check matches for the first length of s1
        matches = 0
        for key in s1_map:
            if s1_map.get(key, 0) == s2_map.get(key, 0):
                matches += 1
        
        # loop through start len of s1 for len of s2 - 1 to find
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == len(s1_map):
                return True
            
            # Add a character on the right
            char_add = s2[r]
            s2_map[char_add] = s2_map.get(char_add, 0) + 1
            if char_add in s1_map:  # mean if char_add affects s1_map
                if s2_map[char_add] == s1_map[char_add]:
                    matches += 1
                elif s2_map[char_add] == s1_map[char_add] + 1:
                    matches -= 1
            
            # Remove a character on the left
            char_remove = s2[l]
            s2_map[char_remove] -= 1
            if char_remove in s1_map:  # mean if char_remove affects s1_map
                if s2_map[char_remove] == s1_map[char_remove]:
                    matches += 1
                elif s2_map[char_remove] == s1_map[char_remove] - 1:
                    matches -= 1
            
            # increase left
            l += 1
        
        return matches == len(s1_map)
