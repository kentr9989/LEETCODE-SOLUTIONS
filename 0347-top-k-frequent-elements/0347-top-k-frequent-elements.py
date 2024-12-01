class Solution:
    def topKFrequent(self,nums: List[int], k:int) -> List[int]:
        # map element by its frequency {key: num , value : freq}
        freq_map = {}
        for num in nums:
            if num not in freq_map:
                freq_map[num] = 0
            freq_map[num] += 1
        print(freq_map)
        # bucket sort arr : {index: freq, value: element with same freq}
        bucket_arr = [[] for i in range(len(nums) + 1)]
        print(bucket_arr)
        for item,value in freq_map.items():
            bucket_arr[value].append(item)
        
        print(bucket_arr)
        
        # start from bottom to top add to res_arr until k hit 0 
        res_arr = []
        for freq in range(len(nums),0,-1):
            for value in bucket_arr[freq]:
                res_arr.append(value)
                k -= 1
                if k == 0:
                    return res_arr
        
        return []
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # map to store frequency
#         map_freq = {}
#         for num in nums:
#             if num in nums:
#                 map_freq[num] = map_freq.get(num,0) + 1
#         print(f"Map freq: {map_freq}")
        
#         # map to store group frequency [arr[]]
#         map_group_freq = [[] for i in range(len(nums) + 1)]
#         for value,freq in map_freq.items():
#             print(value,freq)
#             map_group_freq[freq].append(value)
#         print(f"Map group freq: {map_group_freq}")
        
#         # return k element by looping through map_group_freq
#         res = []
#         count_k = 0
#         for freq in range(len(nums), 0 , -1):
#             print(f"Freq: {freq}")
#             for value in map_group_freq[freq]:
#                 if count_k == k:
#                     return res
#                 count_k += 1
#                 res.append(value)
                
#                 # print(f" res: {res}")
#                 # print(f" value: {value}")
        
       
#         return res
# if __name__ == "__main__":
#     solution = Solution()
#     result = solution.topKFrequent([1],1)
#     print(f"Result: {result}")


# class Solution:
#     # n : length of nums
#     # Time  O(n)
#     # Space complexity : O(n)
#     # by using bucket sort
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
# #         # Create dict freq_count {value : count}
# #         freq_count = {}
# #         # Assign all element to freq_count
# #         for num in nums:
# #             freq_count[num] = freq_count.get(num,0) + 1
                
# #         # Create 2d array freq_array as key and value is the value
# #         # that have the same frequency. The length of array is 
# #         # from 0 -> length of nums because worst case is 1 element
# #         # have occur nums amount of time
# #         freq_array = [[] for i in range(len(nums) + 1)]
                
# #         # Put all the key and value to freq_array
# #         for value,frequency in freq_count.items():
# #             freq_array[frequency].append(value)
            
# #         # Create res array
# #         res = []
        
# #         # Do a 2 for loop from from end to 1
# #         # push the value in to res
# #         # if length of res equal k:
# #         #   return res
# #         for i in range(len(freq_array) -1,0,-1):
# #             for value in freq_array[i]:
# #                 res.append(value)
# #                 if len(res) == k:
# #                     return res
            
            
# #         # return [] assume it doesnt match k
# #         return []

      