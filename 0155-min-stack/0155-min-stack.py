class MinStack:

    def __init__(self):
        # init original stack - empty
        self.stack = []
        # init another min stack - empty
        self.min_stack = []
        
    def push(self, val: int) -> None:
        # append to first stack
        self.stack.append(val)
        # for the second stack: 
        # update the val with top of min_stack if minStack is not empty
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        # append that val to the top min_stack
        self.min_stack.append(val)

    def pop(self) -> None:
        # pop from the first stack
        self.stack.pop()
        # pop from second stack
        self.min_stack.pop()
        
    def top(self) -> int:
        # return top of the first stack
        return self.stack[-1]

    def getMin(self) -> int:
        # return top of the min stack
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()