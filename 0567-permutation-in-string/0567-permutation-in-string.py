class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # Initialize hash maps for character counts
        s1Count, s2Count = {}, {}

        # Populate the hash maps with the initial counts
        for i in range(len(s1)):
            s1Count[s1[i]] = s1Count.get(s1[i], 0) + 1
            s2Count[s2[i]] = s2Count.get(s2[i], 0) + 1

        matches = 0

        # Count how many characters have the same frequency in s1Count and s2Count
        for key in s1Count:
            if s1Count.get(key, 0) == s2Count.get(key, 0):
                matches += 1

        # Sliding window
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == len(s1Count):
                return True

            # Add the new character to the current window
            char = s2[r]
            s2Count[char] = s2Count.get(char, 0) + 1

            if char in s1Count:
                if s2Count[char] == s1Count[char]:
                    matches += 1
                elif s2Count[char] == s1Count[char] + 1:
                    matches -= 1

            # Remove the character left out of the window
            char = s2[l]
            s2Count[char] -= 1

            if char in s1Count:
                if s2Count[char] == s1Count[char]:
                    matches += 1
                elif s2Count[char] == s1Count[char] - 1:
                    matches -= 1

            l += 1

        return matches == len(s1Count)
