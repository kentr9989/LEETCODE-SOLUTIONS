class Solution:
    # Time complexity : O(n)
    # Space complexity: O(1)
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not self.isAlphaNumeric(s[left]):
                left += 1
            while left < right and not self.isAlphaNumeric(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
            
        return True    
                
    def isAlphaNumeric(self, c):
        return (ord("A") <= ord(c) <= ord("Z") or
                ord("a") <= ord(c) <= ord("z") or
                ord("0") <= ord(c) <= ord("9")
                )
            
        
#         # Init left and right pointer
#         l, r = 0 , len(s) -1
        
#         # while left is less than right:
#         #   while left is less than right and not alphanumeric:
#         #       increase left pointer
#         #   while right is greater than left and not alphanumeric:
#         #       decrease right pointer
#         #   if left (lowercase) not equal right (lowercase):
#         #       return False
#         #   decrease right pointer
#         #   increase left pointer
        
#         while l < r:
#             while l < r and not self.alphaNum(s[l]):
#                 l += 1
#             while l < r and not self.alphaNum(s[r]):
#                 r -= 1
#             if s[l].lower() != s[r].lower():
#                 print("left " + s[l])
#                 print("right " + s[r])
#                 return False
#             r -= 1
#             l += 1
#         # return True because all character match
#         return True
    
#     # Function to check whether the character is alphanumeric
#     def alphaNum(self,c) :
#         # return c is between 'A' to 'Z'
#         # or c is between 'a' to 'z'
#         # or c is between '0' to '9'
#         return (ord('A') <= ord(c) <= ord('Z') or
#                 ord('a') <= ord(c) <= ord('z') or
#                 ord('0') <= ord(c) <= ord('9')
#                )