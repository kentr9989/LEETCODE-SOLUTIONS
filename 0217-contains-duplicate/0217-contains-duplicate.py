class Solution:
    def containsDuplicate(self, nums):
        count_freq = {}
        for num in nums:
            if num in count_freq:
                return True
            count_freq[num] = True
        return False
    
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: No duplicates
    nums1 = [1, 2, 3, 4]
    print(f"Test case 1: {solution.containsDuplicate(nums1)}")  # Expected output: False

    # Test case 2: Has duplicates
    nums2 = [1, 2, 3, 1]
    print(f"Test case 2: {solution.containsDuplicate(nums2)}")  # Expected output: True