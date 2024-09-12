class Solution:
    # Time complexity : O(n)
    # Space complexity : O(n)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        
        stack = []
        
        for index,temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stack_index,stack_temp = stack.pop()
                res[stack_index] = index - stack_index
            stack.append([index,temp])
        
        return res
        # # init res array
        # res = [0] * len(temperatures)
        # # init stack of [temp,index]
        # stack = []
        # # iterate index, temp of temperatures:
        # #   while stack is not empty and temp > temp top of stack:
        # #       pop from our stack
        # #       add to res array
        # #   append current index and temp to stack
        # for index,temp in enumerate(temperatures):
        #     while stack and temp > stack[-1][0]:
        #         stack_temp, stack_index = stack.pop()
        #         print(stack_index)
        #         res[stack_index] = index - stack_index
        #     stack.append([temp,index])
        # # return res 
        # # no need to run through res to assign 0 because initially we alrd did
        # return res