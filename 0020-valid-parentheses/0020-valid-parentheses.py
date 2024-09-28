class Solution:
    # Time complexity : O(n)
    # Space complexity : O(n)
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {")" : "(" , "}" : "{", "]" : "["}
        
        for char_s in s:
            if char_s in close_to_open: # close tag
                if stack and close_to_open[char_s] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else: # open tag
                stack.append(char_s)
        
        return len(stack) == 0 # everything is pop
            
            
        
        
        
        
        
        
        
        
        
        
#         stack = []
#         closeToOpen = {")" : "(", "}" : "{", "]": "["}
        
        
#         for char in s:
#             if char in closeToOpen:
#                 if stack and stack[-1] == closeToOpen[char]:
#                     stack.pop()
#                 else:
#                     return False
#             else:
#                 stack.append(char)
            
#         if stack: 
#             return False
#         else:
#             return True
#         # Init stack - python list
#         stack = []
#         # Init hashmap of 3 pair parentheses
#         close_to_open = {")":"(", "}" : "{", "]":"["};
        
#         # loop throught for every character:
#         #   check if character is in closeToOpen hashmap (closed character):
#         #       if stack is not empty and top of stack equal match to close:
#         #           pop from our stack
#         #       else:
#         #           return False because parentheses dont match
#         #   else:
#         #       add that character to the stack
#         for char in s:
#             if char in close_to_open:
#                 if stack and stack[-1] == close_to_open[char]:
#                     stack.pop()
#                 else:
#                     return False
#             else:
#                 stack.append(char)
                
#         # return True if stack is empty otherwise False
#         return True if not stack else False
        