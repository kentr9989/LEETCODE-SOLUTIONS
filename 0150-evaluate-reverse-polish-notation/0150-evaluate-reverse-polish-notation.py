class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def evalRPN(self, tokens: List[str]) -> int:
        # Init stack
        stack = []
        # loop through every character in token:
        #   if character is "+":
        #       pop from our stack twice then add tgt
        #       append result to the stack
        #   else if character is "-":
        #       pop from stack twice then deduct
        #       second number - first number
        #   else if character is "*":
        #   else if character is "/":
        #   else: 
        #       stack append the number (conver to int)
        
        # return top of the stack
        for char in tokens:
            if char == "+":
                stack.append(stack.pop()+stack.pop())
            elif char == "-":
                first,second = stack.pop(), stack.pop()
                stack.append(second - first)
            elif char == "*":
                stack.append(stack.pop() * stack.pop())
            elif char == "/":
                first,second = stack.pop(), stack.pop()
                stack.append(int(second/first)) # convert to 0
            else:
                stack.append(int(char))
        return stack[0]
                
                
                
                
                
                
                