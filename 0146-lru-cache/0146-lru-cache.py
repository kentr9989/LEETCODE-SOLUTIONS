class Node:
      def __init__(self, key, value):
            self.key, self.value = key,value
            self.prev, self.next = None, None
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} #key : value
        self.left, self.right = Node(0,0), Node(0,0) # left is LRU , right is MRU
        self.left.next , self.right.prev = self.right, self.left
        self.cap = capacity
        
    # remove node from list 
    def remove(self,node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
    
    # insert node at the right
    def insert(self,node):
        next, prev = self.right, self.right.prev
        node.next, node.prev = next, prev
        self.right.prev = node
        prev.next = node
        
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1        
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        new_node = Node(key,value)
        
        self.cache[key] = new_node
        self.insert(self.cache[key])
        
        
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        # print(self.cache)
        
        

# if __name__ == "__main__":
    

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)