class Solution:
    # Time + space complexity : O(n)
    # by using bucket sort
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create freq_map {element, count}
        # Put all value to the freq_map
        freq_map = {}
        for num in nums:
            freq_map[num] = 1 + freq_map.get(num,0)
            
        # Init 2d freq array of length of num + 1
        # each element is an array 
        # Put all the value to the freq 2d array
        freq_array = [[] for i in range(len(nums) + 1)]
        for value,frequency in freq_map.items():
            freq_array[frequency].append(value)
      
        # Int res array
        # Loop through the freq array from top to 0:
        #   Loop through the array for each freq index:
        #       push in to res array
        #       if len(res) equal k:
        #           then res
        res = []
        for i in range(len(freq_array) - 1, 0 ,-1) :
            for value in freq_array[i]:
                res.append(value)
                if len(res) == k:
                    return res
        
        # return res
        return res
      