class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [] # pair of [position , speed]
        for i in range(len(position)):
            pair.append([position[i],speed[i]])
        print(f"pair: {pair}")
        
        # sort in reverse order (position come first)
        pair.sort(reverse = True)
        print(f"sorted pair: {pair}")
        
        stack = [] # contains the time to reach destination
        for position,speed in pair:
            stack.append( (target - position) / speed)
            if len(stack) >= 2 and stack[-2] >= stack[-1]: # meaning the one closer to destination have smaller time to reach destination (which mean there is a collide) 
                stack.pop()
                
        return len(stack)