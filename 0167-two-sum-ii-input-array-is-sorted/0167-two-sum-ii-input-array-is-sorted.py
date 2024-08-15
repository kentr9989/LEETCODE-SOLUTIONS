class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Init left pointer = 0
        left = 0
        # Init right pointer = length of numbers - 1
        right = len(numbers) - 1
        
        # Init res array
        # res = []
        
        # while left < right:
        #   if left + right < target:
        #       increment left pointer
        #   else if left + right > target:
        #       decrease right pointer
        #   else:
        #       return [left + 1, right + 1]
        while left < right:
            if (numbers[left] + numbers[right]) < target:
                left += 1
            elif (numbers[left] + numbers[right]) > target:
                print(right)
                right -= 1
            else:
                return [left+1,right+1]
        
        # return res
        return []