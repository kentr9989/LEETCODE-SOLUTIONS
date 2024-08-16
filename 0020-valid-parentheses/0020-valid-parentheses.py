class Solution:
    # Time complexity : O(n)
    # Space complexity : O(n)
    def isValid(self, s: str) -> bool:
        # Init stack - python list
        stack = []
        # Init hashmap of 3 pair parentheses
        close_to_open = {")":"(", "}" : "{", "]":"["};
        
        # loop throught for every character:
        #   check if character is in closeToOpen hashmap (closed character):
        #       if stack is not empty and top of stack equal match to close:
        #           pop from our stack
        #       else:
        #           return False because parentheses dont match
        #   else:
        #       add that character to the stack
        for char in s:
            if char in close_to_open:
                if stack and stack[-1] == close_to_open[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        print(stack)
        # return True if stack is empty otherwise False
        return True if not stack else False
        